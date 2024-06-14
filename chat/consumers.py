import json
from channels.generic.websocket import WebsocketConsumer

class Chat_consumer(WebsocketConsumer):

    def connect(self):
        self.accept()

        self.send(text_data=json.dumps(
            {
                "type": 'connection established',
                "message": 'Hello world!'
            }
        ))
