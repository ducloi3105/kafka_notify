from pynotify.bases.event import BaseEvent
from pynotify.events.notifications import *


class Notifications(BaseEvent):
    def account(self) -> NotificationAccount:
        return NotificationAccount(
            kafka_client=self.kafka_client,
        )

    def auth(self) -> NotificationAuth:
        return NotificationAuth(
            kafka_client=self.kafka_client,
        )

    def admin(self) -> NotificationAdmin:
        return NotificationAdmin(
            kafka_client=self.kafka_client,
        )

    def billing(self) -> NotificationBilling:
        return NotificationBilling(
            kafka_client=self.kafka_client,
        )
