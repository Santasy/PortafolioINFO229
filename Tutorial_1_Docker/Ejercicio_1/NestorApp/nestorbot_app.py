import os
import logging
from flask import Flask # Consultas HTTP
from slack import WebClient
from nestorbot import NestorBot

app = Flask(__name__)
slack_client = WebClient(token=os.environ.get("SLACKBOT_TOKEN"))

def hello(channel):
    nestor = NestorBot(channel)
    slack_client.chat_postMessage(**nestor.get_message_payload())

@app.route("/")
def sendHello():
    return "Hola, soy Nestor"

if __name__ == "__main__":
    channel_call = slack_client.api_call("conversations.list")
    if channel_call.get("ok"):
        for chan in channel_call["channels"]:
            print("Channel: '%s', id = %s" % ( chan["name"], chan["id"]))
    else: print("No se encontraron canales.")
    hello("#playground")

    print("Nestor ha saludado.")
    ### Login ###
    '''
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    #app.run(port=3000)
    app.run(host="0.0.0.0", port=3000)
    '''