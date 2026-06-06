class ControlPlaneAPI:
    def dashboard(self, metrics, cluster_state):
        return {
            "system_status": "ONLINE",
            "metrics": metrics,
            "cluster_nodes": len(cluster_state)
        }
