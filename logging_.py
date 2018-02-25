import logging

# レベル設定もできる
# formatter = '%(levelname)s:%(message)s'
# formatter = '%(asctime)s:%(message)s'
# logging.basicConfig(level = logging.INFO, format = formatter)
logging.basicConfig(level = logging.INFO)

# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info %s %s', 'test', 'test2')
logging.info('info')
# logging.debug('debug')