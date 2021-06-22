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

    def send_event(self, topics, key, payload: dict = None):
        try:
            payload = self._create_payload(payload)
            payload = json.dumps(payload)
            print(f"Send event to kafka | {topics} | {key} ==> {payload}")
            self.producer.send(
                topics,
                key=bytes(key, "utf-8"),
                value=payload,
            )
            self.producer.flush()
        except Exception as e:
            raise ServiceError(f'Send event failed: {e}')
        return True

    @staticmethod
    def _create_payload(payload: dict = None):
        if not payload:
            payload = dict
        now = datetime.utcnow()
        ts = now.replace(tzinfo=timezone.utc)
        print(ts)
        if not payload.get('eventId'):
            payload['eventId'] = f'{str(str(uuid4().hex))}.' \
                                 f'{int(ts.timestamp())}' \
                                 f'@localhost'
        if not payload.get('eventTime'):
            payload['eventTime'] = ts.isoformat()

        return payload
