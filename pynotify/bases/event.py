from pynotify.bases.error.client import ClientError
from datetime import datetime, timezone
from uuid import uuid4


class BaseEvent(object):
    PROJECT_NAME = 'kafkaEvent'

    def __init__(self, kafka_client):
        self.kafka_client = kafka_client

    @staticmethod
    def payload_parser(payload: dict):
        now = datetime.utcnow()
        ts = now.replace(tzinfo=timezone.utc)

        if not payload.get('host'):
            payload['host'] = 'localhost'
        if not payload.get('eventId'):
            payload['eventId'] = f'{str(str(uuid4().hex))}.' \
                                 f'{int(ts.timestamp())}' \
                                 f'@{payload["host"]}'
        if not payload.get('eventTime'):
            payload['eventTime'] = ts.isoformat()

        if 'env' not in payload:
            raise ClientError('Payload: env required')

        if 'service_name' in payload:
            try:
                service_names = payload['service_name'].split('_')
                sns = []
                for i, sn in enumerate(service_names):
                    if i != 0:
                        sn = sn.title()
                    sns.append(sn)

                payload['service_name'] = ''.join(sns)
            except:
                pass
        print(payload)
        return payload
