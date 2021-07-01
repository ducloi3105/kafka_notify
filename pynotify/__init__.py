import json
from kafka import KafkaProducer

from pynotify.bases.error.client import ClientError
from pynotify.bases.client.kafka_client import KafkaClient
from pynotify.events import Notifications


class BizflyNotificationClient(object):
    def __init__(self,
                 kafka_servers: list,
                 kafka_retries: int = 2,
                 kafka_config: dict = None
                 ):
        self.kafka_client = KafkaClient(
            servers=kafka_servers,
            retries=kafka_retries,
            **kafka_config
        )

    def notification(self) -> Notifications:
        return Notifications(
            self.kafka_client,
        )
