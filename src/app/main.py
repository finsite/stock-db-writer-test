from app.logger import setup_logger
from app.writer import write_to_test_db

logger = setup_logger(__name__)

def main() -> None:
    logger.info("Starting test DB writer service...")
    write_to_test_db({})  # Example call

if __name__ == "__main__":
    main()
