import logging

logger = logging.getLogger(__name__)


class ExcludeHealthEndpoint(logging.Filter):
    ENDPOINT = "health"

    def filter(self, record: logging.LogRecord) -> bool:
        logging.info(
            f"ExcludeHealthEndpoin received record={record} with message {record.getMessage()}"
        )
        return self.ENDPOINT not in record.getMessage()
