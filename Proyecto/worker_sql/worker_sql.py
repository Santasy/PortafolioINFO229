from sqlite3.dbapi2 import Error
import pika 
import sqlite3
from datetime import date

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
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

#Este se cambia segun corresponda
channel.queue_declare(queue='save_on_database')

def callback(ch, method, props, body):
    #Logica de guardar todos los mensajes de Slack
    #el body deberia ser una lista de strings
    #[canalSlack, userName, message]
    canalSlack, userName, message = body.decode()

    #Conexion mediante SQL
    slackdb = sqlite3.connect('slack_messages.db')
    try:
        #Cursor
        cur = slackdb.cursor()

        #Logica de Tablas
        if not cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(canalSlack)).fetchone():
            #La tabla aun no se crea
            cur.execute("CREATE TABLE {}(nombre text PRIMARY KEY, fecha date, message text)".format(canalSlack))

        DATE = str(date.today())

        #Ingreso de Mensaje a la tabla del canal
        cur.execute("INSERT INTO {} VALUES({}, {}, {})".format(canalSlack, userName, DATE, message))
        
    except Error:
        print(Error)

    finally:
        slackdb.close()

channel.basic_consume(queue='save_on_database', on_message_callback=callback)
print(' [*] Esperando Mensajes')