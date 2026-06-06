class SharedState:
    def __init__(self):
        self.global_events = []

    def append(self, event):
        self.global_events.append(event)

    def snapshot(self):
        return {
            "event_count": len(self.global_events),
            "latest_event": self.global_events[-1] if self.global_events else None
        }
