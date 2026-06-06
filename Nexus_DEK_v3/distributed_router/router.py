class DistributedRouter:
    def route(self, event, cluster_state):
        best_node = None
        lowest_load = 999

        for node_id, node in cluster_state.items():
            if node["status"] != "ACTIVE":
                continue

            load = node["meta"]["capacity"]

            if load < lowest_load:
                lowest_load = load
                best_node = node_id

        return best_node
