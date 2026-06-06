import uuid
import time

class WorkerNode:
    def __init__(self):
        self.id = f"worker_{uuid.uuid4().hex[:8]}"
        self.alive = True
        self.load = 0
        self.failures = 0

    def heartbeat(self):
        return {
            "id": self.id,
            "alive": self.alive,
            "load": self.load,
            "failures": self.failures
        }

    def process(self, event):
        self.load += 1
        try:
            time.sleep(0.05)
            return {"status": "processed", "worker": self.id}
        except Exception:
            self.failures += 1
            self.alive = False
            raise

    def self_heal(self):
        if self.failures > 0:
            self.alive = True
            self.failures = 0
            self.load = 0
