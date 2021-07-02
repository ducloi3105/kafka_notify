from pynotify.bases.event import BaseEvent


class NotificationWebmail(BaseEvent):
    PROJECT_NAME = 'webmail'

    def message_created(self, topic, email, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.webmail.message_updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=email,
            payload=payload
        )

    def message_updated(self, topic, email, payload):
        payload = self.payload_parser(payload)
        payload['eventName'] = f"{payload['env']}.{self.PROJECT_NAME}.webmail.message_updated"

        return self.kafka_client.send_event(
            topic=topic,
            key=email,
            payload=payload
        )
