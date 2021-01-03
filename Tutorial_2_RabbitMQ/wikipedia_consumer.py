import pika
import sys
import wikipedia

wikipedia.set_lang("es")

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(
    exchange='direct_querys', exchange_type='direct')

wiki_queue = channel.queue_declare(queue='', exclusive=True)
queue_name = wiki_queue.method.queue

channel.queue_bind(
    exchange='direct_querys', queue=queue_name, routing_key='wikipedia')
print(' [Wikipedia] Waiting. To exit press CTRL+C')

def callback(ch, method, properties, body):
    query = body.decode("utf-8") # body comes as bytes
    print(" [Wikipedia] %r:" % (query))
    result = wikipedia.summary(wikipedia.search(query)[0], sentences=3, auto_suggest=False)
    print(result)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()