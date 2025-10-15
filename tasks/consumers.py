import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "tasks_group"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):

await self.channellayer.groupdiscard(self.groupname, self.channelname)

    async def taskupdate(self, event):
        message = event.get("message", "")
        await self.send(textdata=json.dumps({"message": message}))
