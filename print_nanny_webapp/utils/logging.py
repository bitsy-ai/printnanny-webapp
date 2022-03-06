import logging

logger = logging.getLogger(__name__)


class ExcludeHealthEndpoint(logging.Filter):
    def filter(self, record):
        return record.getMessage().find("/health") == -1


logging.getLogger("uvicorn.access").addFilter(ExcludeHealthEndpoint())
