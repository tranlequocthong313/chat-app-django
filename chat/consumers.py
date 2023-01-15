import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    """
    Consumer aka View in Django
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = None

    async def connect(self) -> None:
        if self.scope["user"].is_anonymous:
            await self.close()
        else:
            await self.accept_connection()

    async def accept_connection(self):
        """
        Connect user to group
        """
        self.group_name = "chat_" + self.scope["url_route"]["kwargs"]["room_name"]
        await self.channel_layer.group_add(self.group_name, self.channel_name)  # type: ignore
        await self.accept()

    @database_sync_to_async
    def save_message(self, message) -> None:
        """
        Save new message to database
        """
        Message.objects.create(
            content=message["content"],
            author_id=message["authorID"],
            room_id=message["roomID"],
        )

    async def disconnect(self, code) -> None:
        await self.channel_layer.group_discard(self.group_name, self.channel_name)  # type: ignore

    async def receive(self, text_data=None, bytes_data=None) -> None:
        if text_data:
            await self.save_message(json.loads(text_data))
        data = {}
        data["type"] = "send_message_to_all_channels_in_group"
        data["data"] = text_data
        await self.channel_layer.group_send(self.group_name, data)  # type: ignore

    async def send_message_to_all_channels_in_group(self, event) -> None:
        """
        Send message to current group
        """
        data = {}
        data["type"] = "broadcast"
        data["message"] = event["data"]
        await self.send(text_data=json.dumps(data))
