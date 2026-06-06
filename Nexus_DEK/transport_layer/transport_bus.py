import asyncio
import queue

class TransportBus:
    def __init__(self):
        self.event_queue = asyncio.Queue()

    async def publish(self, event):
        await self.event_queue.put(event)

    async def consume(self):
        return await self.event_queue.get()
