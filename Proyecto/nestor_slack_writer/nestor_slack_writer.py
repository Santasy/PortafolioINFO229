import pika
import time
import os
from slack import WebClient

time.sleep(15)
try:
    CANAL_SLACK = "#playground"

    ##### CONNEXIÓN A SLACK ########

    # Create a slack client
    slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

    ########## ESPERA Y PUBLICA UN MENSAJE EN SLACK CUANDO RECIBE UN MENSAJE ####

    def callback(ch, method, properties, body):
        text = body.decode()
        message = {
                "channel": CANAL_SLACK,
                "blocks": [
                    {"type": "section", "text": {"type": "mrkdwn", "text": text}},
                ],
            }
        #PUBLICACION DEL MENSAJE EN SLACK
        slack_web_client.chat_postMessage(**message)

    ########### CONNEXIÓN A RABBIT MQ #######################\
    print(" [*] Does this fail?")
    HOST = os.environ['RABBITMQ_HOST']

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=HOST))
    channel = connection.channel()

    #El consumidor utiliza el exchange 'nestor'
    channel.exchange_declare(exchange='nestor', exchange_type='topic', durable=True)

    #Se crea un cola temporaria exclusiva para este consumidor (búzon de correos)
    result = channel.queue_declare(queue="publicar_slack", exclusive=True, durable=True)
    queue_name = result.method.queue

    #La cola se asigna a un 'exchange'
    channel.queue_bind(exchange='nestor', queue=queue_name, routing_key="publicar_slack")

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(" [*] Ready to write!")

    channel.start_consuming()
except Exception as err:
    exception_type = type(err).__name__
    print(" [!] FATAL ERROR: %s", exception_type)