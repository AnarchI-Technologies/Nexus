import uuid
import datetime

class EventKernel:
    SCHEMA_VERSION = "1.0"

    def create_event(self, tenant_id, event_type, payload):
        return {
            "event_id": f"evt_{uuid.uuid4().hex[:12]}",
            "schema_version": self.SCHEMA_VERSION,
            "tenant_id": tenant_id,
            "event_type": event_type,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "state": "CREATED",
            "payload": payload
        }

    def validate(self, event, allowed_types):
        if event["event_type"] not in allowed_types:
            raise ValueError("Invalid event type")
        return True
