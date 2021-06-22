from pynotify.bases.event import BaseEvent


class NotificationBilling(BaseEvent):
    def account_created(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def account_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def trial_created(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def trial_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def trial_upgraded(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def payment_created(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def balance_adjusment_created(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def invoice_created(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def invoice_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def balance_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )
