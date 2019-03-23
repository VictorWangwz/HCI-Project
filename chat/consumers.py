__author__ = ' Zhen Wang'

# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message'] if 'message' in text_data_json.keys() else ""
        exit = 0
        if "exit" in text_data_json.keys():
            exit = text_data_json["exit"]
        if exit == 0:
            reply = {
                'type': 'chat_message',
                "message": message,
                "name": text_data_json['name'],
                "media":  text_data_json["media"],
                "exit": exit
            }
        else:
            reply =   {
                'type': 'chat_message',
                "message": message,
                "name": text_data_json['name'],
                "exit": exit
            }

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            reply
        )

    # Receive message from room group
    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))