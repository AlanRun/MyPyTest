"""
This module contains the paths to various directories and files used in the project.
"""
import os

current = os.path.abspath(__file__)
# print(f'Current directory: {current}')

BASE_DIR = os.getcwd()
# print(f'Base directory: {BASE_DIR}')

# Define the path to the config file
# _config_path = BASE_DIR + os.sep + 'config'
_config_path = BASE_DIR
# print(f'Config path: {_config_path}')

_testcases_path = BASE_DIR + os.sep + 'testcases'
# print(f'Testcases path: {_testcases_path}')

# Define the path to the config file
_config_file = _config_path + os.sep + 'config.yaml'
# print(f'Config file path: {_config_file}')

# Define the path to the extract file
_extract_file = BASE_DIR + os.sep + 'extract.yaml'

# Define the path to the data directory
_data_path = BASE_DIR + os.sep + 'data'
# print(f'Data path: {_data_path}')

# Define the path to the log directory
_log_path = BASE_DIR + os.sep + 'logs'
# print(f'log path: {_log_path}')

# Define the path to the utils directory
_utils_path = BASE_DIR + os.sep + 'common'
# print(f'Utils path: {_utils_path}')

# Define the path to the reports directory
_reports_path = BASE_DIR + os.sep +'reports'
# print(f'Reports path: {_reports_path}')

# Define the path to the requirements.txt file
_requirements_path = BASE_DIR + os.sep +'requirements.txt'
# print(f'Requirements path: {_requirements_path}')

# Define the path to the README.md file
_readme_path = BASE_DIR + os.sep + 'README.md'
# print(f'README path: {_readme_path}')

# Define the path to the .gitignore file
_gitignore_path = BASE_DIR + os.sep + '.gitignore'
# print(f'.gitignore path: {_gitignore_path}')


def get_report_path():
    return _reports_path


def get_config_path():
    return _config_path


def get_testcases_path():
    return _testcases_path


def get_config_file():
    return _config_file


def get_extract_file():
    return _extract_file


def get_log_path():
    return _log_path


def get_utils_path():
    return _utils_path


def get_requirements_path():
    return _requirements_path


def get_readme_path():
    return _readme_path


def get_gitignore_path():
    return _gitignore_path


if __name__ == '__main__':
    print('***********')
