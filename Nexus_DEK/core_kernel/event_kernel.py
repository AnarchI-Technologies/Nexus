import uuid
import datetime

class EventKernel:
    def create_event(self, tenant_id: str, event_type: str, payload: dict) -> dict:
        return {
            "event_id": f"evt_{uuid.uuid4().hex[:12]}",
            "tenant_id": tenant_id,
            "event_type": event_type,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "state": "CREATED",
            "payload": payload
        }

    def validate_event(self, event: dict, allowed_types: list) -> dict:
        if event["event_type"] not in allowed_types:
            raise ValueError("Invalid event type")
        return event
