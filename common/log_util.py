import datetime
import logging
import os

from common.config_util import ConfigUtil
from common.dir_util import get_log_path

log_l = {
    'info': logging.INFO,
    'debug': logging.DEBUG,
    'warning': logging.WARNING,
    'error': logging.ERROR
}


class LogUtil:
    def __init__(self, log_file, log_name, log_level):
        self.log_file = log_file
        self.log_name = log_name
        self.log_level = log_level

        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(log_l[self.log_level])

        # 创建一个handler，用于写入日志文件
        if not self.logger.handlers:
            # 定义handler的输出格式
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            fh = logging.FileHandler(filename=self.log_file, encoding='UTF-8')
            fh.setLevel(log_l[self.log_level])
            fh.setFormatter(formatter)

            # 给logger添加handler
            self.logger.addHandler(fh)

            # 创建一个handler，用于将日志输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(log_l[self.log_level])
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

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


log_path = get_log_path()

current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

log_extension = ConfigUtil().get_conf_log_extension()

logfile = os.path.join(log_path, f'{current_time}{log_extension}')

loglevel = ConfigUtil().get_conf_log()


def my_log(log_name=__file__):
    return LogUtil(logfile, log_name, loglevel).logger


if __name__ == '__main__':
    my_log().info('test')
