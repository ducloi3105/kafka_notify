from pynotify.bases.event import BaseEvent


class NotificationAccount(BaseEvent):
    PROJECT_NAME = 'account'

    def updated(self, topic, tenant_id, payload):
        # todo: update verifyPhone, verifyEmail, verifyPayment, twoFactor.updated, password
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )
