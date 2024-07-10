import json

from channels.generic.websocket import WebsocketConsumer


class WsConsumer(WebsocketConsumer):
    def connect(self):
        print(self.scope["url_route"])
        print(self.scope)
        print(self.scope["query_string"])
        self.user = self.scope["user"]
        print(self.user)
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        print(text_data)

        self.send(
            text_data=json.dumps({"message": "收到了" + text_data}, ensure_ascii=False)
        )
