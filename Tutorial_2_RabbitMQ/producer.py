import pika
import sys

if len(sys.argv) < 3:
    print(f"Error, run: {sys.argv[0]} wikipedia|youtube search")
else:
    destiny = sys.argv[1]
    if destiny not in ["wikipedia", "youtube"]:
        print("Error, destiny not valid.")
        exit()
    search = ' '.join(sys.argv[2:])

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(
        exchange='direct_querys', exchange_type='direct')
    
    channel.basic_publish(
        exchange='direct_querys', routing_key=destiny, body=search)
    print(" [x] Sent %r:%r" % (destiny, search))

    connection.close()
