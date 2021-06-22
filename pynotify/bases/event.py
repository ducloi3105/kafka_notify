
class BaseEvent(object):
    def __init__(self, kafka_client):
        self.kafka_client = kafka_client
