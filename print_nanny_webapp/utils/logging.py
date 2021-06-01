import logging


class ExcludeHealthEndpoint(logging.Filter):
    ENDPOINT = "health/"

    def filter(self, record: logging.LogRecord):
        return self.ENDPOINT not in record.getMessage()
