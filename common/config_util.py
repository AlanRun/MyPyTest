from common.yaml_util import read_config


class ConfigUtil:
    def __init__(self):
        self.config = read_config()

    def get_conf_log(self):
        return self.config['BASE']['log_level']

    def get_conf_log_extension(self):
        return self.config['BASE']['log_extension']

    def get_email_config(self):
        return self.config['EMAIL']

    def get_env_config(self, env):
        return self.config[env]

    def get_env_db_config(self, env):
        return self.config[env]['db']

    def get_env_base_url(self, env):
        return self.config[env]['base_url']