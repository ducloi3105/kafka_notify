from pynotify.bases.event import BaseEvent


class NotificationAuth(BaseEvent):
    def created(self, topics, tenant_id, payload):
        # todo: create user -> send info
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def logged_in(self, topics, tenant_id, payload):
        # todo: account logged
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )
