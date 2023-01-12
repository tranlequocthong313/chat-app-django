# This file is corresponding with "views.py" of Django

import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    """
    This will handle all messages from clients, and
    also broadcast them to other clients in this consumer
    """

    def connect(self):
        self.room_group_name = "test"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

        self.send(
            text_data=json.dumps(
                {
                    "type": "connection_success",
                    "status_code": 200,
                    "message": "Connect successfully!",
                    "room_name": self.room_group_name,
                }
            )
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {"type": "chat_message", "message": message},
        )

    def chat_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps({"type": "chat", "message": message}))
