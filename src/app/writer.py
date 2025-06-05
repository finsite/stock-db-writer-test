from app.logger import setup_logger

logger = setup_logger(__name__)

def write_to_test_db(data: dict) -> None:
    logger.info("Writing data to test database (no-op): %s", data)
    # Simulate DB write or log only
