class MetricsEngine:
    def calculate(self, events, errors, nodes):
        return {
            "throughput": len(events),
            "error_rate": errors / max(len(events), 1),
            "node_count": len(nodes)
        }
