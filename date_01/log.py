import logging
import logging.handlers

logger = logging.getLogger()

# 系统默认的logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    filename='log.txt', filemode='a')

# # 1\自定义logging
# logger1 = logging.getLogger('mylogging')
# logger1.setLevel(logging.DEBUG)
#
# # 2\创建一个handler，用于输出到控制台
# c1 = logging.StreamHandler()
#
# # 3\定义c1事件的输出格式Formatter()
# f1 = logging.Formatter('%(asctime)s %(name)s %(message)s')
# c1.setFormatter(f1)
#
# # 4\将c1.handler绑定到自定义logger1
# logger1.addHandler(c1)
#
# # 5、创建RotatingFileHandler处理
# # 导入 import logging.handlers
# # 写入文件，如果文件超过100个Bytes，仅保留5个文件。
# handler = logging.handlers.RotatingFileHandler(
#     'log.txt', maxBytes=100, backupCount=5)
#
# # 6、绑定事件
# logger1.addHandler(handler)
#
# logger1.debug('logger1 debug message')
# logger1.info('logger1 info message')
# logger1.warning('logger1 warning message')
# logger1.error('logger1 error message')
# logger1.critical('logger1 critical message')
