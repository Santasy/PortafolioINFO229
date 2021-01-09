from sqlite3.dbapi2 import Error
import pika 
import sqlite3
from datetime import date
import time
import os

time.sleep(15)
'''
El enunciado del worker dice que se guarden TODOS los mensajes,
por lo que no se espera demasiado parseo por parte del productor.
Se espera recibir el canal de Slack, el Dueño del mensaje y su mensaje. 
Todo esto lo entrega el 'payload' de Slack
La Fecha puede calcularse aqui mismo

Se busca hacer una tabla General, una para cada Canal de Slack,
con el siguiente orden:
|----------|-----------|------------------------------------|
|Nombre    |Fecha      |Mensaje                             |
|----------|-----------|------------------------------------|
|"FelipeL" |2021-01-01 |"Esto es un mensaje de Prueba"      |
|----------|-----------|------------------------------------|
'''
#Conexion a RabbitMQ

HOST = os.environ['RABBITMQ_HOST']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

#El consumidor utiliza el exchange 'nestor'
channel.exchange_declare(exchange='nestor', exchange_type='topic', durable=True)

#Se crea un cola temporaria exclusiva para este consumidor (búzon de correos)
result = channel.queue_declare(queue="sqlite", exclusive=True, durable=True)
queue_name = result.method.queue

#La cola se asigna a un 'exchange'
channel.queue_bind(exchange='nestor', queue=queue_name, routing_key="sqlite")

#Conexion mediante SQL
slackdb = sqlite3.connect('slack_messages.db')
#Cursor
cur = slackdb.cursor()

def callback(ch, method, props, body):
    #Logica de guardar todos los mensajes de Slack
    #el body deberia ser una lista de strings
    query = body.decode()
    data = query.split("$$")
    l = len(data)
    if l == 3:
        canalSlack, userId, message = data
        print(f"[Insert]:\n\t{canalSlack}\n\t{userId}\n\t{message}")

        try:
            #Logica de Tablas
            if not cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(canalSlack)).fetchone():
                #La tabla aun no se crea
                cur.execute("CREATE TABLE '{}' ('id' INTEGER PRIMARY KEY, 'user_id' TEXT, 'message' TEXT)".format(canalSlack))

            #Ingreso de Mensaje a la tabla del canal
            cur.execute("INSERT INTO {} VALUES(null, '{}', '{}')".format(canalSlack, userId, message))
            slackdb.commit()
            
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
    elif l == 2:
        canalSlack, userId = data
        print(f"[GET] {userId} on {canalSlack}")

        try:
            #Ingreso de Mensaje a la tabla del canal
            cur.execute("SELECT * FROM {} WHERE user_id='{}'".format(canalSlack, userId))
            rows = cur.fetchall()

            # -- Send to write --
            # Rows: id, user_id, text
            text = "User {}\n".format(userId)
            for row in rows:
                text += "\t{}\n".format(row[2])
            
            channel.basic_publish(
                exchange='nestor',
                routing_key="publicar_slack",
                body=text
            )
            
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
    else:
        print(" [X] Not prepared for this.")

channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
)
print(' [*] Esperando Mensajes')

channel.start_consuming()