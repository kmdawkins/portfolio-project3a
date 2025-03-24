from loguru import logger
import sys


def setup_logger(log_path: str = "logs/default.log", level: str = "INFO"):
    logger.remove()
    logger.add(sys.stdout, level=level)
    logger.add(log_path, level=level, rotation="10 MB", retention="7 days", compression="zip")