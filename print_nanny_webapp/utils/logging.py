import logging
from django.utils.log import AdminEmailHandler
from django.core.cache import cache

logger = logging.getLogger(__name__)


class ExcludeHealthEndpoint(logging.Filter):
    def filter(self, record):
        return record.getMessage().find("/health") == -1


logging.getLogger("uvicorn.access").addFilter(ExcludeHealthEndpoint())


class ThrottledAdminEmailHandler(AdminEmailHandler):
    PERIOD_LENGTH_IN_SECONDS = 600
    MAX_EMAILS_IN_PERIOD = 3
    COUNTER_CACHE_KEY = "email_admins_counter"

    def increment_counter(self):
        try:
            cache.incr(self.COUNTER_CACHE_KEY)
        except ValueError:
            cache.set(self.COUNTER_CACHE_KEY, 1, self.PERIOD_LENGTH_IN_SECONDS)
        return cache.get(self.COUNTER_CACHE_KEY)

    def emit(self, record):
        try:
            counter = self.increment_counter()
        except Exception as e:
            logger.error("Exception raised in ThrottledAdminEmailHandler %s", e)
        else:
            if counter > self.MAX_EMAILS_IN_PERIOD:
                return
        super(ThrottledAdminEmailHandler, self).emit(record)
