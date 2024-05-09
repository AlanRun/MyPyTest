from common.yaml_util import YamlReader
from common.dir_util import get_config_file, get_db_config_file


class ConfigUtil:
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()
        self.db_config = YamlReader(get_db_config_file()).data()

    def get_conf_log(self):
        return self.config['BASE']['log_level']

    def get_conf_log_extension(self):
        return self.config['BASE']['log_extension']

    def get_db_conf_info(self, db_name):
        return self.db_config[db_name]

    def get_email_config(self):
        return self.config['EMAIL']