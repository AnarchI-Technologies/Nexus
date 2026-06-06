import asyncio

class EventBus:
    def __init__(self):
        self.queue = asyncio.Queue()
        self.subscribers = []

    async def publish(self, event):
        await self.queue.put(event)

    async def subscribe(self):
        return await self.queue.get()
