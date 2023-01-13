import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    """
    Consumer aka View in Django
    """

    async def connect(self) -> None:
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)  # type: ignore
        await self.accept()

    async def disconnect(self, code) -> None:
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)  # type: ignore

    async def receive(self, text_data=None, bytes_data=None) -> None:
        if text_data:
            await self.save_message(json.loads(text_data))
        await self.channel_layer.group_send(  # type: ignore
            self.room_group_name,
            {
                "type": "send_message_to_all_channels_in_group",
                "data": text_data,
            },
        )

    @database_sync_to_async
    def save_message(self, message) -> None:
        """
        Save new message to database
        """
        Message(
            content=message["content"],
            author_id=message["authorID"],
            room_id=message["roomID"],
        ).save()

    async def send_message_to_all_channels_in_group(self, event) -> None:
        """
        Send message to current group
        """
        await self.send(
            text_data=json.dumps(
                {
                    "type": "broadcast",
                    "message": event["data"],
                }
            )
        )
