from kafka import KafkaProducer, KafkaConsumer
import json
import time
from uuid import uuid4
from datetime import datetime, timezone

from pynotify.bases.error.service import ServiceError


class KafkaClient(object):
    def __init__(self, servers: list, retries: int, config=None):
        if not config:
            config = {}
        producer = KafkaProducer(
            bootstrap_servers=servers,
            value_serializer=lambda x: json.dumps(x).encode("utf-8"),
            retries=retries,
            **config
        )
        self.producer = producer
        self.producer = producer

    def send_event(self, topic, key, payload: dict = None):
        try:
            print(f"Send event to kafka | {topic} | {key} ==> {payload}")
            self.producer.send(
                topic,
                key=bytes(key, "utf-8"),
                value=payload,
            )
            self.producer.flush()
        except Exception as e:
            raise ServiceError(f'Send event failed: {e}')
        return True
