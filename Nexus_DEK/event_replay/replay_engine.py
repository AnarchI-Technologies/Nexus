class EventReplayEngine:
    def replay(self, event_log):
        state = []
        for event in event_log:
            state.append(event)
        return state
