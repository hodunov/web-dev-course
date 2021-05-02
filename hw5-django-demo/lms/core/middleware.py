from django.utils.deprecation import MiddlewareMixin
import datetime
from core.models import Logger


class DjangoLogMiddleware(MiddlewareMixin):
    """
    Logs parameters request.path, request.method, execution_time (diff),
    if the request was NOT to admin page (/admin/)
    """
    def process_request(self, request):
        request.start_time = datetime.datetime.now()

    def process_response(self, request, response):
        request.execution_time = datetime.datetime.now() - request.start_time
        if not request.path.startswith('/admin'):
            Logger.objects.create(
                created_at=datetime.datetime.now(),
                request_path=request.path,
                request_method=request.method,
                request_execution_time=request.execution_time.total_seconds(),
            )
        return response
