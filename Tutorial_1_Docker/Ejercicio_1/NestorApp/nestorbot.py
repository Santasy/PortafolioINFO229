import random
import pymongo
import os

DATABASE="nestor"
COLLECTION="frases"

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
                self._choose_message()
            ]
        }

    def getCustomBlock(self):
        text = "Un texto: " + ["TextoA", "TextoB"][random.randint(0, 1)]
        return self.textToBlock(text)

    def _choose_message(self):
        # Conexion MONGO
        myclient = pymongo.MongoClient(host=os.environ['MONGO_HOST'], port=int(os.environ['MONGO_PORT']))
        db = myclient[DATABASE]
        collection = db[COLLECTION]
        
        # Consulta mongo:
        var = [{'$sample': {'size': 1}}]
        results = collection.aggregate(var)
        # Parse:
        text = " "
        for doc in results:
            text = doc["text"]
        print(f'Will send: {text}')
        return self.textToBlock(text)