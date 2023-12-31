import json

from channels.generic.websocket import WebsocketConsumer


class WsConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        print(text_data)

        self.send(text_data=json.dumps({"message": "收到了" + text_data}, ensure_ascii=False))
