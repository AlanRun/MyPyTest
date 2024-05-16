# import json

# import jsonpath

# from debug_talk import DebugTalk


# def is_json(my_str):
#     try:
#         json_obj = json.loads(my_str)
#     except ValueError as e:
#         return False
#     return True


# class JsonUtil:
#
#     def find_paths_by_value(self, json_obj, target_value, current_path=[], result=[], target_value_start=None,
#                             target_value_end=None, target_value_contains=None):
#         if isinstance(json_obj, dict):
#             for key, value in json_obj.items():
#                 next_path = current_path + [key]
#                 if (value == target_value if target_value else False) \
#                         or (target_value_contains in str(value) if target_value_contains else False) \
#                         or (str(value).startswith(target_value_start) if target_value_start else False and str(value).endswith(target_value_end) if target_value_end else False):
#                     result.append(next_path)
#                 else:
#                     self.find_paths_by_value(value, target_value, next_path, result, target_value_start,
#                                              target_value_end, target_value_contains)
#         elif isinstance(json_obj, list):
#             for index, value in enumerate(json_obj):
#                 next_path = current_path + [index]
#                 if value == target_value:
#                     result.append(next_path)
#                 else:
#                     self.find_paths_by_value(value, target_value, next_path, result, target_value_start,
#                                              target_value_end, target_value_contains)
#
#     def get_path_by_value(self, json_obj, target_v=None, v_start=None, v_end=None, v_contains=None):
#         """
#         Get all paths by the value in a JSON object.
#         :param json_obj: Target JSON object
#         :param target_v: Target value
#         :param v_start:
#         :param v_end:
#         :param v_contains:
#         :return: list of JSON paths
#         """
#         ps = []
#         self.find_paths_by_value(json_obj, target_v, result=ps, target_value_start=v_start, target_value_end=v_end,
#                                  target_value_contains=v_contains)
#         jes = ['$.' + '.'.join(map(str, path)) for path in ps]
#         for p in jes:
#             print(p, jsonpath.jsonpath(json_obj, p))
#         return jes
#
#     def print_json(self, json_obj, path=''):
#         if isinstance(json_obj, dict):
#             for key, value in json_obj.items():
#                 self.print_json(value, f'{path}.{key}' if path else key)
#         elif isinstance(json_obj, list):
#             for index, value in enumerate(json_obj):
#                 self.print_json(value, f'{path}.{index}' if path else str(index))
#         else:
#             jp = '$.' + path
#             print(f'{jp}: {json_obj}')
#             print(f'{jp}: {jsonpath.jsonpath(your_json, jp)}')


# def find_and_replace(data, target_value=None, target_value_start=None,
#                      target_value_end=None, target_value_contains=None):
#     """
#     热加载替换JSON中的变量
#     :param data: Target object, dict or list
#     :param target_value: Target value
#     :param target_value_start: Target value start with
#     :param target_value_end: Target value end with
#     :param target_value_contains: Target value contains
#     :return:
#     """
#     if isinstance(data, dict):
#         for key, value in data.items():
#             if isinstance(value, dict):
#                 find_and_replace(value, target_value, target_value_start, target_value_end, target_value_contains)
#             elif isinstance(value, list):
#                 find_and_replace(value, target_value, target_value_start, target_value_end, target_value_contains)
#             if (value == target_value if target_value else False) \
#                     or (target_value_contains in str(value) if target_value_contains else False) \
#                     or (target_value_start in str(value) if target_value_start else False and target_value_end in str(value) if target_value_end else False):
#                 func_name = value[value.index(target_value_start)+len(target_value_start):value.index('(')]
#                 arg_value = value[value.index('(') + 1:value.index(')')]
#                 new_value = getattr(DebugTalk(), func_name)(*arg_value.split(',') if arg_value != '' else [])
#                 if value[:value.index(target_value_start)] or value[value.index(target_value_end):]:
#                     data[key] = value[:value.index(target_value_start)] + (new_value if new_value else '') + value[value.index(target_value_end)+len(target_value_end):]
#                     # print(f'\n{key}: {data[key]}')
#                 else:
#                     data[key] = new_value if new_value else ''
#             else:
#                 find_and_replace(value, target_value, target_value_start, target_value_end, target_value_contains)
#     elif isinstance(data, list):
#         for item in data:
#             find_and_replace(item, target_value, target_value_start, target_value_end, target_value_contains)


# your_json = {"name": "Test Request API 3", "description": "Test the API for requesting a test case3", "request": {"url": "https://postman-echo.com/get", "method": "GET", "params": {"foo1": "bar1", "foo2": "foo2_${get_random_str(1000, 9999)}", "foo3": "${get_random_num(1000, 9999)}"}, "response": {"status_code": 200, "body": {"message": "Test case request submitted successfully. We will get back to you soon."}}, "validate": [{"contains": {"$.url": "https://postman-echo.com/get"}}, {"eq": {"$.args.foo1": "bar1"}}]}}


# if __name__ == '__main__':
#     # print_json(your_json)
#     # t_v = "Bob"
#     # t_v = "${get_random_str(1000, 9999)}"
#     t_v_start = "${"
#     t_v_end = "}"
#     find_and_replace(your_json, target_value_start=t_v_start, target_value_end=t_v_end)
#     print(f'\nyour_json: {json.dumps(your_json)}')
#     # JsonUtil().get_path_by_value(your_json, v_start=t_v_start, v_end=t_v_end)

