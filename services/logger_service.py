# python modules
import logging
from datetime import datetime as dt
import os
"""
logger function
"""
LOGGER_LEVEL = os.getenv('LOGGER_LEVEL', 10)
logger = logging.getLogger('werkzeug')
base = 'logs/'
monthDir = dt.now().strftime('%Y-%m/')
baseAndMonthDir = base + monthDir
if not os.path.exists(baseAndMonthDir):
    os.makedirs(baseAndMonthDir)
serviceName = 'SS-CES'
fileName = serviceName + '--' + dt.now().strftime('%d-%B-%Y') + ".log"
fullPath = baseAndMonthDir + fileName

handler = logging.FileHandler(fullPath)
formatter = logging.Formatter('%(levelname)s: [%(asctime)s] %(funcName)s(%(lineno)d) -- %(message)s',
                              datefmt='%d/%b %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(LOGGER_LEVEL)
