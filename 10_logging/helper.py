import logging
logger = logging.getLogger(__name__)
logger.propagate = False # nothing gets logs, it doesn't propogate to our base logger
logger.info('hello from helper')