import random

class NestorBot:
    _BASE_BLOCK = { 
        "type": "section",
        "text": { 
            "type": "mrkdwn",
            "text": "Nestor ya no es James"
        }
    }

    def __init__(self, channel):
        self.channel = channel

    def textToBlock(self, text):
        return { 
            "type": "section", 
            "text": { "type": "mrkdwn", 
                "text": f"{text}"
            }
        }

    def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                self._BASE_BLOCK,
                self.getCustomBlock()
            ]
        }

    def getCustomBlock(self):
        text = "Un texto: " + ["TextoA", "TextoB"][random.randint(0, 1)]
        return self.textToBlock(text)