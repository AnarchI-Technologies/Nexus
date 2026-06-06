class ControlPlaneAPI:
    def system_status(self, workers):
        return {
            "worker_count": len(workers),
            "system_health": "GREEN" if len(workers) > 0 else "DEGRADED"
        }
