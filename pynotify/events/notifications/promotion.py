from pynotify.bases.error.client import ClientError
from pynotify.bases.event import BaseEvent


class NotificationPromotion(BaseEvent):
    PROJECT_NAME = 'promotion'
