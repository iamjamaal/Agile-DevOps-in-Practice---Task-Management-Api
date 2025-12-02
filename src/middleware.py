# Create middleware for request logging
import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from src.logging_config import logger


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    '''Middleware to log all requests and responses'''

    async def dispatch(self, request: Request, call_next):
        # Generate request ID
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id

        # Log request
        logger.info(
            'Request started',
            extra={
                'request_id': request_id,
                'method': request.method,
                'path': request.url.path,
                'client': request.client.host if request.client else 'unknown'
            }
        )

        # Track time
        start_time = time.time()

        # Process request
        try:
            response = await call_next(request)
            process_time = time.time() - start_time

            # Log response
            logger.info(
                'Request completed',
                extra={
                    'request_id': request_id,
                    'method': request.method,
                    'path': request.url.path,
                    'status_code': response.status_code,
                    'process_time': f'{process_time:.3f}s'
                }
            )

            # Add request ID to response headers
            response.headers['X-Request-ID'] = request_id

            return response

        except Exception as e:
            process_time = time.time() - start_time

            # Log error
            logger.error(
                'Request failed',
                extra={
                    'request_id': request_id,
                    'method': request.method,
                    'path': request.url.path,
                    'error': str(e),
                    'process_time': f'{process_time:.3f}s'
                },
                exc_info=True
            )
            raise
