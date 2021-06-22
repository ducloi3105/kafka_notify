from pynotify.bases.error import BaseError


class ClientError(BaseError):
    pass


class InvalidParams(ClientError):
    pass


class ClientNotAvailable(ClientError):
    pass


class AuthenticationFailed(ClientError):
    pass


class SessionError(ClientError):
    pass


class RecordNotFound(ClientError):
    pass
