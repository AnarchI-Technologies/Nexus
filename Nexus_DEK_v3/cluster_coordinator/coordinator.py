import time

class ClusterCoordinator:
    def __init__(self):
        self.nodes = {}

    def register_node(self, node_id, meta):
        self.nodes[node_id] = {
            "meta": meta,
            "last_heartbeat": time.time(),
            "status": "ACTIVE"
        }

    def heartbeat(self, node_id):
        if node_id in self.nodes:
            self.nodes[node_id]["last_heartbeat"] = time.time()

    def detect_failures(self, timeout=5):
        dead = []
        now = time.time()

        for node_id, data in self.nodes.items():
            if now - data["last_heartbeat"] > timeout:
                data["status"] = "DEAD"
                dead.append(node_id)

        return dead
