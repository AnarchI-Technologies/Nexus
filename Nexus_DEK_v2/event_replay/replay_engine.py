class EventReplayEngine:
    def replay(self, event_log):
        state = []
        for event in event_log:
            state.append({
                "event_id": event["event_id"],
                "state": event.get("state", "UNKNOWN")
            })
        return state
