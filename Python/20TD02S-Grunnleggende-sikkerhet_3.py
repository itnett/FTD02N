python
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)

logger = setup_logging()

def perform_sensitive_operation():
    logger.info("Sensitive operation started")
    # Perform the operation
    logger.info("Sensitive operation completed")

# Example usage
perform_sensitive_operation()