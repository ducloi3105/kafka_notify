from pynotify.bases.event import BaseEvent
from pynotify.bases.error.client import ClientError

class NotificationAdmin(BaseEvent):
    PROJECT_NAME = 'admin'

    def account_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.account.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def service_auto_scale_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.service.autoScale.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def service_backup_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.service.backup.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def service_call_center_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.service.callCenter.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def service_cdn_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.service.cdn.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def service_cloud_drive_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.service.cloudDrive.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def service_container_registry_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.service.containerRegistry.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def service_ddos_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.service.ddos.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def service_kubernetes_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.service.kubernetes.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def service_load_balancer_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.service.loadBalancer.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def service_mail_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.service.mail.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def service_cloud_server_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.service.cloudServer.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def service_simple_storage_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.service.simpleStorage.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def service_vpn_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.service.vpn.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def manage_blocked_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.manage.blocked.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def manage_dashboard_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.manage.dashboard.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def manage_images_updated(self, topic, tenant_id, payload):
        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def manage_network_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.manage.network.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def manage_service_catalog_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.manage.serviceCatalog.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def manage_whitelist_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.manage.whitelist.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def manage_whitelist_created(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.manage.whitelist.created"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def manage_whitelist_deleted(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.manage.whitelist.deleted"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def billing_trial_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        if not payload.get('service_name'):
            raise ClientError('Payload: service_name required')
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.billing.trial.{payload['service_name']}.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def billing_balance_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.billing.balance.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )

    def billing_invoice_updated(self, topic, tenant_id, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.billing.invoice.updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=tenant_id,
            payload=payload
        )
