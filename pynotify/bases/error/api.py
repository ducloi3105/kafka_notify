from pynotify.bases.error import BaseError


class HTTPError(BaseError):
    status_code = 500

    def output(self):
        data = super(HTTPError, self).output()
        data['status_code'] = self.status_code
        return data


class MethodNotAllowed(HTTPError):
    status_code = 405
    message = 'Method not allowed.'


class Unauthorized(HTTPError):
    status_code = 401
    message = 'Unauthorized error.'


class BadRequestParams(HTTPError):
    status_code = 400
    message = 'Bad request params.'


class PermissionError(HTTPError):
    status_code = 403
    message = 'Permission error.'


class ApiSessionError(HTTPError):
    status_code = 499
    message = 'Api session is expired or not found.'


class ServiceNotAvailable(HTTPError):
    status_code = 503
    message = 'Service not available.'


class ServerError(HTTPError):
    status_code = 500
    message = 'Server error.'
