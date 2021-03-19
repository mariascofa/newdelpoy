from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin
import logging

logging.basicConfig(filename='example.log', level=logging.INFO)


class LogMiddleware(MiddlewareMixin):
    """Writes logs about received request and response."""

    def process_request(self, request):
        """Collects detailed request info and writes it into logs."""
        resolved_path_info = resolve(request.path_info)
        logging.info(
            'Request %s View name %s route %s',
            request, resolved_path_info.view_name, resolved_path_info.route)

    def process_response(self, request, response):
        """Gets response info and writes it into logs."""
        logging.info('For request %s response is %s', request, response)
        return response


class RawDataMiddleware(MiddlewareMixin):
    """Gets request info, puts it into the hash and writes logs about it."""

    def process_request(self, request):
        """Creates hash value to identify the request and add this
        hash value to request.META so that it can be used as a response."""
        resolved_path_info = resolve(request.path_info)
        hash_request = hash(resolved_path_info.route)
        logging.info(
            'Hash value for request is %s', hash_request)
        request.META['hashed'] = hash_request


class IdentifyResponseMiddleware(MiddlewareMixin):
    """Adds to each response a hem value that was
    created at the time of receiving the request (RawDataMiddleware)."""

    def process_response(self, request, response):
        """Gets response info and writes it into logs.
        Gets info about hashed request from META and shows connection
        between hash_request and response."""
        hash_request = request.META['hashed']
        logging.info(
            'For hashed request %s response is %s', hash_request, response)
        return response
