from pynotify.bases.event import BaseEvent


class NotificationBilling(BaseEvent):
    def account_created(self, topic, tenant_id, payload):
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def account_updated(self, topic, tenant_id, payload):
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def trial_created(self, topic, tenant_id, payload):
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def trial_updated(self, topic, tenant_id, payload):
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def trial_upgraded(self, topic, tenant_id, payload):
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def payment_created(self, topic, tenant_id, payload):
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def balance_adjusment_created(self, topic, tenant_id, payload):
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def invoice_created(self, topic, tenant_id, payload):
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def invoice_updated(self, topic, tenant_id, payload):
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def balance_updated(self, topic, tenant_id, payload):
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )
