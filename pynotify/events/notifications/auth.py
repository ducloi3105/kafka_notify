from pynotify.bases.event import BaseEvent


class NotificationAuth(BaseEvent):
    PROJECT_NAME = 'auth'

    def created(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.account.created"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.auth.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def logged_in(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.account.loggedIn"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )
