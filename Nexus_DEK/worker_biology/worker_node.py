import uuid
import time

class WorkerNode:
    def __init__(self):
        self.id = f"worker_{uuid.uuid4().hex[:8]}"
        self.alive = True
        self.load = 0

    def heartbeat(self):
        return {"id": self.id, "alive": self.alive, "load": self.load}

    def self_heal(self):
        if not self.alive:
            self.alive = True
            self.load = 0

    def process(self, event):
        self.load += 1
        time.sleep(0.1)
        self.load -= 1
        return {"status": "processed", "worker": self.id}
