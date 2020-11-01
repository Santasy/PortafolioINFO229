from slack import WebClient
from nestorbot import NestorBot
import os

slack_web_client = WebClient(token=os.environ.get("SLACKBOT_TOKEN"))
nestor = NestorBot("#playground")
""" # Basic Example
message = nestor.get_message_payload()
slack_web_client.chat_postMessage(**message) # ** individualiza la lista
"""

slack_web_client.chat_postMessage(**({
    "channel": nestor.channel,
    "blocks": [
        nestor.textToBlock("Probando textToBlock()")
    ]
}))