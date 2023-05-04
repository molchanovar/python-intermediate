# Diff log levels, diff conf options, how to log in diff modules, log handlers
# Capture stack traces, how to rotating file handler 


# === Levels ===
# by default only warnings or above are printed

import logging

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
DATEFMT = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt=DATEFMT)

import helper
# 2023-05-04 12:51:03 - helper - INFO - hello from helper
# log name change to 'helper'

# logging.debug('This id a debug message')
# logging.info('This id a info message')
# logging.warning('This id a warning message')
# logging.error('This id a error message')
# logging.critical('This id a critical message')


# ==== Log handlers === 