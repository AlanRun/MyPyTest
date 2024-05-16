import importlib
import inspect
import os

import jinja2
import yaml
# import copy
import json
import allure

# from typing import Text, Dict, Union

from common.dir_util import get_testcases_path, get_extract_file, get_config_file
# from common.json_util import find_and_replace


def is_json(my_str):
    try:
        json.loads(my_str)
    except ValueError as e:
        return False
    return True


def get_crp():
    # 获取当前文件所在的目录
    current_directory = os.path.abspath(os.path.dirname(__file__))
    return current_directory


@allure.step('读取yaml文件')
def read_yaml(file, key=None):
    if os.path.exists(file):
        with open(file, encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key] if key else value
    else:
        raise FileNotFoundError('文件不存在')


@allure.step('读取config yaml文件')
def read_config():
    """
    read config_yaml file
    :return: config, type:dict
    """
    file = get_config_file()
    if os.path.exists(file):
        with open(file, encoding='utf-8') as f:
            config = yaml.load(stream=f, Loader=yaml.FullLoader)
            return config
    else:
        raise FileNotFoundError('文件不存在')


@allure.step('写入yaml文件')
def write_yaml(data):
    """
    写入yaml文件
    :param data:
    :return:
    """
    file = get_extract_file()
    if os.path.exists(file):
        with open(file, mode='a', encoding='utf-8', ) as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)
    else:
        raise FileNotFoundError('文件不存在')


@allure.step('清空yaml文件')
def clear_yaml():
    """
    清空yaml文件
    :return:
    """
    file = get_extract_file()
    if os.path.exists(file):
        with open(file, mode='w', encoding='utf-8') as f:
            f.truncate()
    else:
        raise FileNotFoundError('文件不存在')


def render(tpl_path, **kwargs):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')).get_template(filename).render(**kwargs)


def all_functions():
    debug_module = importlib.import_module('debug_talk')
    all_function = inspect.getmembers(debug_module, inspect.isfunction)
    print(dict(all_function))
    return dict(all_function)


@allure.step('读取testcase yaml文件')
def read_testcase(yaml_name):
    """
    read ./testcase/yaml_name file
    :param yaml_name:
    :return:
    """
    file = get_testcases_path() + os.sep + yaml_name
    if os.path.exists(file):
        # 热加载，替换{{func()}}中的函数调用
        r = render(file, **all_functions())
        return yaml.safe_load(r)
        # with open(file, encoding='utf-8') as f:
        #     args = yaml.load(stream=f, Loader=yaml.FullLoader)
        #     return args
    else:
        raise FileNotFoundError('文件不存在')


# def replace_load(data: Union[Dict, Text]) -> Union[Dict, Text]:
#     """
#     热加载，替换${func()}中的函数调用
#     :param data: 传入数据参数，可以是字典或文本类型
#     :return: 对测试用例进行热加载
#     """
#
#     data_obj = copy.deepcopy(data) if data else False  # 这里可以考虑使用deepcopy来进行深拷贝，防止原数据被修改
#     if isinstance(data, str):  # 如果data不为空，并且格式为字符串,尝试将其转换为字典或列表
#         try:
#             data_obj = json.loads(data_obj)
#         except json.JSONDecodeError:
#             pass
#
#     t_v_start = "${"
#     t_v_end = "}"
#
#     find_and_replace(data_obj, target_value_start=t_v_start, target_value_end=t_v_end)
#     return data_obj




# class YamlReader:
#     def __init__(self, yamlf):
#         if os.path.exists(yamlf):
#             self.yamlf = yamlf
#         else:
#             raise FileNotFoundError('文件不存在')
#         self._data = None
#         self._data_all = None
#
#     def data(self):
#         if not self._data:
#             with open(self.yamlf, 'rb', encoding='utf-8') as f:
#                 self._data = yaml.safe_load(f)
#         return self._data
#
#     def data_all(self):
#         if not self._data_all:
#             with open(self.yamlf, 'rb', encoding='utf-8') as f:
#                 self._data_all = yaml.safe_load_all(f)
#         return self._data_all

