from pynotify.bases.event import BaseEvent
from pynotify.events.notifications import (
    NotificationAdmin,
    NotificationSuggestion,
    NotificationBilling,
    NotificationPromotion,
    NotificationAuth,
    NotificationAccount,
    NotificationWebmail,
)


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

    def suggestion(self) -> NotificationSuggestion:
        return NotificationSuggestion(
            kafka_client=self.kafka_client,
        )

    def promotion(self) -> NotificationPromotion:
        return NotificationPromotion(
            kafka_client=self.kafka_client,
        )

    def webmail(self) -> NotificationWebmail:
        return NotificationWebmail(
            kafka_client=self.kafka_client,
        )
