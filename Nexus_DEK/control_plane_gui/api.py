class ControlPlaneAPI:
    def get_system_status(self, workers):
        return {
            "worker_count": len(workers),
            "system_health": "STABLE"
        }
