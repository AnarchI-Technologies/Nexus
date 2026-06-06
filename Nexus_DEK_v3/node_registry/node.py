import uuid

class NodeRegistry:
    def __init__(self):
        self.node_id = f"node_{uuid.uuid4().hex[:8]}"
        self.capacity = 1.0
        self.status = "JOINING"

    def join_cluster(self, coordinator):
        coordinator.register_node(self.node_id, {
            "capacity": self.capacity
        })
        self.status = "ACTIVE"
        return self.node_id
