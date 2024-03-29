

# https://docs.python.org/3/howto/logging.html


import logging


logger = logging.getLogger(name='myLogger')
logger.setLevel(level=logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(level=logging.DEBUG)


# create file handler and set level to debug
fh = logging.FileHandler(
    filename='/home/manu/git_repos/utility_func/example.log')
fh.setLevel(level=logging.DEBUG)

# create formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# add formatter to ch
ch.setFormatter(fmt=formatter)
fh.setFormatter(fmt=formatter)

# add ch to logger
logger.addHandler(hdlr=ch)
logger.addHandler(hdlr=fh)


# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
