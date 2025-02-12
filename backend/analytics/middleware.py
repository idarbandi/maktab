# analytics/middleware.py
import logging

from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class AnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        user = request.user if request.user.is_authenticated else 'Anonymous'
        logger.info(
            f'User: {user}, Path: {request.path}, Method: {request.method}, Status: {response.status_code}')

        return response


# Checking Users Authority


class AdminCheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff):
            request.is_admin = True
        else:
            request.is_admin = False
