from pynotify.bases.event import BaseEvent


class NotificationAccount(BaseEvent):
    def updated(self, topics, tenant_id, payload):
        # todo: update verifyPhone, verifyEmail, verifyPayment, twoFactor.updated, password
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )
