from pynotify.bases.error.client import ClientError
from pynotify.bases.event import BaseEvent


class NotificationSuggestion(BaseEvent):
    PROJECT_NAME = 'suggestion'

    def check_balance(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.checkBalance.created"
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )
