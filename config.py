import logging
import logging.config

logging.config.fileConfig('logger.conf')

logger = logging.getLogger('example')

logger.debug('this is example debugmessage')
