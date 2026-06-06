class EventStream:
    def __init__(self):
        self.events = []

    def ingest(self, event):
        self.events.append(event)

    def filter_by_tenant(self, tenant_id):
        return [e for e in self.events if e["tenant_id"] == tenant_id]
