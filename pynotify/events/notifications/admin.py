from pynotify.bases.event import BaseEvent


class NotificationAdmin(BaseEvent):
    def account_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def service_autoscale_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def service_backup_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def service_callcenter_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def service_cdn_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def service_cloud_drive_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def service_container_registry_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def service_ddos_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def service_kubernetes_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def service__updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def service_load_balancer_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def service_mail_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def service_cloud_server_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def service_simple_storage_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def service_vpn_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def manage_blocked_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def manage_dashboard_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def manage_images_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def manage_network_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def manage_service_catalog_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def manage_whitelist_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def manage_whitelist_created(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def manage_whitelist_deleted(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def billing_trial_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def billing_balance_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )

    def billing_invoice_updated(self, topics, tenant_id, payload):
        return self.kafka_client.send_event(
            topics=topics,
            key=tenant_id,
            payload=payload
        )
