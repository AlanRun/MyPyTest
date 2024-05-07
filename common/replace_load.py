import copy
import json

from typing import Text, Dict, Union

import allure

from common.json_util import find_and_replace


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

# def replace_load(data: Union[Dict, Text]) -> Union[Dict, Text]:
#     """
#
#     :param data: 传入数据参数，可以是字典或文本类型
#     :return: 对测试用例进行热加载
#     """
#     # 不管什么类型，统一转换为字符串格式
#
#     if data and isinstance(data, dict):  # 如果data不为空，并且格式为字典,转换为字符串格式
#         # ensure_ascii=False,避免将中文转换为Unicode编码，但是兼容可能会有问题
#         # str_data = json.dumps(data, ensure_ascii=False)
#         # 先将json字符串进行encode()编码，然后再使用unicode_escape编解码器将Unicode编码转换回中文字符
#         str_data = json.dumps(data).encode().decode('unicode_escape')
#     else:
#         str_data = str(data)
#     # 替换值
#     if str_data is not None and "${" in str_data and "}" in str_data:
#         for i in range(1, str_data.count("${") + 1):
#             if "${" in str_data and "}" in str_data:
#                 start_index = str_data.index("${")
#                 end_index = str_data.index("}", start_index)
#                 # 字符串切片：切片从开始索引开始截取到结束索引，不包含结束索引（俗称含头不含尾），步长就是每几步取一个
#                 old_value = str_data[start_index:end_index + 1]
#                 func_name = old_value[2:old_value.index('(')]
#                 arg_value = old_value[old_value.index('(') + 1:old_value.index(')')]
#                 new_value = getattr(DebugTalk(), func_name)(*arg_value.split(','))
#                 print(f"\n替换前：{old_value},\n替换后：{new_value},\n type:{type(new_value)}")
#                 str_data = str_data.replace(old_value, str(new_value))
#     # 还原数据类型
#     if data and isinstance(data, dict):  # 如果data为字典，则将str_data还原为字典
#         data = json.loads(str_data)
#     else:
#         data = str_data
#     # 返回替换过后的data
#     return data
