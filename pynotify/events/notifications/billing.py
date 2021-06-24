from pynotify.bases.error.client import ClientError
from pynotify.bases.event import BaseEvent


class NotificationBilling(BaseEvent):
    PROJECT_NAME = 'billing'

    def account_created(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.account.created"
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def account_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.account.updated"
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def trial_created(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        if not payload.get('service_name'):
            raise ClientError('Payload: service_name required')
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.trial.{payload['service_name']}.created"
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def trial_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        if not payload.get('service_name'):
            raise ClientError('Payload: service_name required')
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.trial.{payload['service_name']}.updated"
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def trial_upgraded(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        if not payload.get('service_name'):
            raise ClientError('Payload: service_name required')
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.trial.{payload['service_name']}.upgraded"
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def payment_created(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.payment.created"
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def balance_adjustment_created(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.balanceAdjustment.created"
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def invoice_created(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.invoice.created"
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def invoice_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.invoice.updated"
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def balance_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.balanceA.updated"
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )
