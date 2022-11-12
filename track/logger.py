import logging

logging.basicConfig(
    level=logging.ERROR,
    filemode="w",
    format="%(asctime)s - %(filename)s.%(funcName)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("test_logger")
