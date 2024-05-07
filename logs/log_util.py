import logging
import os


class LogUtil:
    def __init__(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(os.getcwd() + '/log.txt', encoding='UTF-8')
        fh.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        # 给logger添加handler
        logger.addHandler(fh)

        # 创建一个handler，用于将日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        self.logger = logger

    def get_logger(self):
        if not self.logger:
            self.logger = logging.getLogger(__name__)
        return self.logger

    def log_info(self, message):
        self.logger.info(message)

    def log_debug(self, message):
        self.logger.debug(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_warning(self, message):
        self.logger.warning(message)


if __name__ == '__main__':
    LogUtil().log_info('这是一个info级别的日志信息')
    LogUtil().log_debug('这是一个debug级别的日志信息')
    LogUtil().log_error('这是一个error级别的日志信息')