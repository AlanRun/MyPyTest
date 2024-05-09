import os

import yaml
import copy
import json
import allure

from typing import Text, Dict, Union
from common.json_util import find_and_replace


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
    with open(os.getcwd()) as file:
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
    with open(os.getcwd() + '/extract.yaml', mode='w', encoding='utf-8') as file:
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
        if args:
            if isinstance(args, list):
                for item in args:
                    new_item = replace_load(item)
                    args[args.index(item)] = new_item
            elif isinstance(args, dict):
                for key, value in args.items():
                    new_item = replace_load(value)
                    args[key] = new_item
        else:
            return None
        return args


@allure.step("替换yaml中的函数调用")
def replace_load(data: Union[Dict, Text]) -> Union[Dict, Text]:
    """
    热加载，替换${func()}中的函数调用
    :param data: 传入数据参数，可以是字典或文本类型
    :return: 对测试用例进行热加载
    """

    data_obj = copy.deepcopy(data) if data else False  # 这里可以考虑使用deepcopy来进行深拷贝，防止原数据被修改
    if isinstance(data, str):  # 如果data不为空，并且格式为字符串,尝试将其转换为字典或列表
        try:
            data_obj = json.loads(data_obj)
        except json.JSONDecodeError:
            pass

    t_v_start = "${"
    t_v_end = "}"

    find_and_replace(data_obj, target_value_start=t_v_start, target_value_end=t_v_end)
    return data_obj


class YamlReader:
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在')
        self._data = None
        self._data_all = None

    def data(self):
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = yaml.safe_load(f)
        return self._data

    def data_all(self):
        if not self._data_all:
            with open(self.yamlf, 'rb') as f:
                self._data_all = yaml.safe_load_all(f)
        return self._data_all

