import pika
import sys
import time
import os
import logging
from flask import Flask
from slackeventsapi import SlackEventAdapter
from slack import WebClient

time.sleep(17)

############ CONEXION RABBITMQ ##############

HOST = os.environ['RABBITMQ_HOST']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

#Creamos el exchange 'nestor' de tipo 'topic'
channel.exchange_declare(exchange='nestor', exchange_type='topic', durable=True)

########### APLICACION WEB FLASK ############

# Initialize a Flask app to host the events adapter
app = Flask(__name__)
# Create an events adapter and register it to an endpoint in the slack app for event injestion.
slack_events_adapter = SlackEventAdapter(os.environ.get("SLACK_SIGNING_SECRET"), "/slack/events", app)

print(os.environ.get("SLACK_SIGNING_SECRET"))

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

print(os.environ.get("SLACK_TOKEN"))

# List of users
users = []

# An example of one of your Flask app's routes
@app.route("/")
def hello():
  return "Hello there!"

@slack_events_adapter.on("message")
def message(payload):
    """Parse the message event
    """
  
    # Get the event data from the payload
    print("Payload:")
    print(payload)
    event = payload.get("event", {})

    # Get the text from the event that came through
    text = event.get("text")
    
    if text.startswith("[help]"):
        channel.basic_publish(
            exchange='nestor',
            routing_key="publicar_slack",
            body=(
                "Comandos disponibles:\n" +
                "[mensajes] <id_usuario>\n" +
                "\tUsuarios disponibles:\n\t" +
                "\n\t".join(users)
            )
        )

    if text.startswith("[mensajes]"):
        user = text.split(" ")[1]
        if user in users:
            channel.basic_publish(
                exchange='nestor',
                routing_key="sqlite",
                body="playground$$"+user)
        else:
            channel.basic_publish(
                exchange='nestor',
                routing_key="publicar_slack",
                body="Usuario no reconocido."
            )

# Funcion que revisa el historial de mensajes
def checkHistory(channel_id):
    response = slack_web_client.conversations_history(
        channel=channel_id,
        limit=20 # Para facilitar las pruebas 
    )

    # El ultimo mensaje esta al inicio,
    # asi que se reversa el arreglo
    messagges = response["messages"]
    print(" [R] Retrieved %d messages.\n" % (len(messagges)))
    invalid_message = "No se puede mostrar este contenido."
    for mssg in messagges:
        # Add user if neccesary
        user = mssg["user"]
        if user not in users:
            users.append(user)

        # Check message
        if mssg["text"] == invalid_message:
            # Try reading blocks
            print(" - [Complex message] %s:" % (user))
            try:
                if mssg["blocks"]:
                    for block in mssg["blocks"]:
                        try:
                            text = block["text"]["text"]
                            print("  *", text)
                        except:
                            print("  * [Can't read block.]")
                else:
                    print(" - No tiene bloques")
            except:
                print(" - [E] Can't read 'blocks'.")
        else: # Normal message
            text = mssg["text"]
            print(" - %s: %s" % (user, text))
        channel.basic_publish(
            exchange='nestor',
            routing_key="sqlite",
            body="$$".join(["playground", user, text]))
    print(" [R] %d users found." % (len(users)))

if __name__ == "__main__":

    # Revisa el historial de mensajes
    playground_channel_id = "C01C8434J85"
    checkHistory(playground_channel_id)

    # Run our app on our externally facing IP address on port 3000 instead of
    # running it on localhost, which is traditional for development.
    app.run(host='0.0.0.0', port=3000)
