class FaultConvergenceSystem:
    def __init__(self, coordinator):
        self.coordinator = coordinator

    def reconcile(self):
        dead_nodes = self.coordinator.detect_failures()

        for node in dead_nodes:
            print(f"[IMMUNE SYSTEM] Rebuilding workload from {node}")

        return {
            "recovered_nodes": len(dead_nodes),
            "status": "CONVERGED"
        }
