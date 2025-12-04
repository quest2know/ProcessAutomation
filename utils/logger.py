import logging


def setup_logger(log_file: str, level=logging.INFO):
    """Sets up a logger that writes to the specified log file."""
    logger = logging.getLogger(log_file)
    logger.setLevel(level)

    # Create file handler which logs even debug messages
    fh = logging.FileHandler(log_file)
    fh.setLevel(level)

    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
    logger.info(f"Logger initialized, logging to {log_file}")
