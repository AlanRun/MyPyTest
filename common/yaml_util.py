import json
import os

import allure
import yaml

from common.replace_load import replace_load

file_path = r'D:\Develop\Project\ApiTest\extract.yaml'


def get_crp():
    # 获取当前文件所在的目录
    current_directory = os.path.abspath(os.path.dirname(__file__))
    return current_directory


@allure.step('读取yaml文件')
def read_yaml(key):
    """
    读取yaml文件
    :param key:
    :return:
    """
    with open(file_path) as file:
        value = yaml.load(stream=file, Loader=yaml.FullLoader)
        return value[key]


@allure.step('写入yaml文件')
def write_yaml(data):
    """
    写入yaml文件
    :param data:
    :return:
    """
    with open(os.getcwd() + '/extract.yaml', mode='a', encoding='utf-8') as file:
        yaml.dump(data=data, stream=file, allow_unicode=True)


@allure.step('清空yaml文件')
def clear_yaml():
    """
    清空yaml文件
    :return:
    """
    with open(file_path, mode='w', encoding='utf-8') as file:
        file.truncate()


@allure.step('读取testcase yaml文件')
def read_testcase(yaml_name):
    """
    读取testcase yaml文件
    :param yaml_name:
    :return:
    """
    with open(os.getcwd() + '/testcases/' + yaml_name) as file:
        args = yaml.load(stream=file, Loader=yaml.FullLoader)
        args_str = json.dumps(args)
        for item in args:
            new_item = replace_load(item)
            # args_str = args_str.replace(json.dumps(item), json.dumps(new_item))
            args[args.index(item)] = new_item
        args = json.loads(args_str)
        # 返回替换过后的args
        return args
