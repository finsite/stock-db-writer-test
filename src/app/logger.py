import logging
import os

def setup_logger(name: str = "app") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        log_level = os.getenv("LOG_LEVEL", "INFO").upper()
        logger.setLevel(getattr(logging, log_level, logging.INFO))
    return logger
