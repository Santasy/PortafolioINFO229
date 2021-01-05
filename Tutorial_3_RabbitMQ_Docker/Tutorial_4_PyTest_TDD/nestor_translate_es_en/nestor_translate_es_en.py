#!/usr/bin/env python
import pika
import time
import os
import transformers
from transformers import pipeline
from transformers import AutoModelWithLMHead, AutoTokenizer, MarianTokenizer, MarianMTModel

########### CONFIGURACION MODELO DE TRADUCCION AUTOMATICA ##########


model_name = "Helsinki-NLP/opus-mt-es-en"

tokenizer = MarianTokenizer.from_pretrained(model_name)

model = MarianMTModel.from_pretrained(model_name)

###################################################################

#time.sleep(10)

########### CONNEXIÓN A RABBIT MQ #######################
HOST = os.environ['RABBITMQ_HOST']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

#El consumidor utiliza el exchange 'nestor'
channel.exchange_declare(exchange='nestor', exchange_type='topic', durable=True)

#Se crea un cola temporaria exclusiva para este consumidor (búzon de correos)
result = channel.queue_declare(queue="traducir", exclusive=True, durable=True)
queue_name = result.method.queue

#La cola se asigna a un 'exchange'
channel.queue_bind(exchange='nestor', queue=queue_name, routing_key="traducir")


##########################################################


########## ESPERA Y HACE UN BUSQUEDA WIKIPEDIA CUANDO RECIBE UN MENSAJE ####

print(' Nestor_Translate_Es_En Waiting for messages...')


def callback(ch, method, properties, body):
    query = body.decode()
    if query.startswith("[traducir]") and len(str(body))<300:
        query = query[10:]
        print(query)
        to_translate = [query]

        translated = model.generate(**tokenizer.prepare_translation_batch(to_translate))
        result = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]

        print(result[0])

        ########## PUBLICA EL RESULTADO COMO EVENTO EN RABBITMQ ##########
        channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body="traducción es->en:"+str(result[0]))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

###########################################################
