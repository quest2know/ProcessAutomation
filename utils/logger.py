import logging
from logging.handlers import RotatingFileHandler


def setup_logger(log_file: str, level=logging.INFO):
    """Sets up a logger that writes to the specified log file."""
    logger = logging.getLogger(log_file)
    logger.setLevel(logging.INFO)

    # 🔥 Prevent duplicate handlers
    if not logger.handlers:
        handler = RotatingFileHandler(
            log_file,
            maxBytes=5_000_000,
            backupCount=5,
            encoding="utf-8"
        )

        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s - %(name)s - %(message)s"
        )
        handler.setFormatter(formatter)

        logger.addHandler(handler)

    logger.propagate = False  # Avoid logging twice via root

    return logger
