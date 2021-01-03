import pika
import sys
from apiclient.discovery import build
from apiclient.errors import HttpError

# Youtube Setup
DEVELOPER_KEY = "AIzaSyAC2usKjdwhCT69uqLzgHjEt-HfgFwdqjE"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY )

def youtube_search(query):
    response = youtube.search().list(
        q=query,
        part="id,snippet",
        maxResults=5,
        type="video"
    ).execute()

    results = []
    for search_result in response.get("items", []):
        results.append(" - " + search_result["snippet"]["title"])
    return results

def callback(ch, method, properties, body):
    query = body.decode('utf-8')
    try:
        results = youtube_search(query)
        print(
            " [Youtube] %r:\n" % (query),
            "\n".join(results) )
    except HttpError as exc:
        print("Error %d:\n%s" % (exc.resp.status, exc.content))    

# RabbitMQ setup
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(
    exchange='direct_querys', exchange_type='direct')

youtube_queue = channel.queue_declare(queue='', exclusive=True)
queue_name = youtube_queue.method.queue

channel.queue_bind(
    exchange='direct_querys', queue=queue_name, routing_key='youtube')

# Ready to consume
print(' [Youtube] Waiting. To exit press CTRL+C')

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()