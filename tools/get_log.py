import logging.handlers
import os
from config import BASE_PATH


class GetLog:
    # 新建一个日志器变量
    __logger = None

    @classmethod
    def get_log(cls):
        if cls.__logger is None:
            # 获取日志器
            cls.__logger = logging.getLogger('admin')

            # 设置日志级别
            cls.__logger.setLevel(logging.INFO)

            # 获取处理器
            log_path = BASE_PATH + os.sep + 'log' + os.sep + 'hmtt.log'
            th = logging.handlers.TimedRotatingFileHandler(filename=log_path, when='midnight', interval=1, backupCount=30, encoding='utf-8')
            err_log_path = BASE_PATH + os.sep + 'log' + os.sep + 'hmtt_err.log'
            th2 = logging.handlers.TimedRotatingFileHandler(filename=err_log_path, when='midnight', interval=1, backupCount=30, encoding='utf-8')

            # 单独设置th2处理器日志级别为error
            th2.setLevel(logging.ERROR)

            # 设置格式器
            fmt = fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)

            # 将格式器添加到处理器中
            th.setFormatter(fm)
            th2.setFormatter(fm)

            # 将处理器添加到logger
            cls.__logger.addHandler(th)
            cls.__logger.addHandler(th2)
        # 返回日志器
        return cls.__logger


if __name__ == '__main__':
    log = GetLog.get_log()
    log.info('info信息')