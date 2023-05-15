# Diff log levels, diff conf options, how to log in diff modules, log handlers
# Capture stack traces, how to rotating file handler 


# === Levels ===
# by default only warnings or above are printed

# import logging

# FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# DATEFMT = '%Y-%m-%d %H:%M:%S'
# logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt=DATEFMT)

# import helper
# 2023-05-04 12:51:03 - helper - INFO - hello from helper
# log name change to 'helper'

# logging.debug('This id a debug message')
# logging.info('This id a info message')
# logging.warning('This id a warning message')
# logging.error('This id a error message')
# logging.critical('This id a critical message')


## ==== Capturing stack traces in locks ==== 
# import logging

# try: 
#     a = [1,2,3]
#     val = a[4]
# except IndexError as e:
#     # logging.error(e) # ERROR:root:list index out of range
#     logging.error(e, exc_info=True) # add val = a[4] to print (helps in troubleshootings)


# import logging
# import traceback

# try:
#     a = [1,2,3]
#     val = a[4]
# except:
#     logging.error("The error is %s", traceback.format_exc()) # ERROR:root:The error is Traceback



# ==== rotating file handler by SIZE ====
# import logging
# from logging.handlers import RotatingFileHandler

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# # roll over after 2KB, and keep backup logs app.log.1, app.log.2, etc
# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# logger.addHandler(handler)

# for _ in range(10000):      # '_' means - we don't care about this
#     logger.info('Hello, world')



# ==== rotating file handler by TIME ====
import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s, m, h, d, midnight, w0
handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info('Hello, world')
    time.sleep(5)
