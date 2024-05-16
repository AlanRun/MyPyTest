"""
This file is used to define fixtures for the test cases.
"""
import pytest

from common.yaml_util import clear_yaml
from common.log_util import my_log


# def pytest_addoption(parser):
#     parser.addini("env", "设置env")
#     # parser.addoption("env", action="store", default="dev", help="设置env")


@pytest.fixture(scope='class', autouse=True)
def class_fixture(request):
    my_log().info(f"Starting Class:{request.cls.__name__}")
    clear_yaml()
    yield
    my_log().info(f"Finished Class:{request.cls.__name__}")


# @pytest.fixture(scope='class')
# def args_fixture(request, ini, env_vars):
#     """
#     This fixture is used to get the arguments from ini file and environment variables.
#     :param request:
#     :param ini: ConfigParser配置对象，可以使用ini.get(section, option)来获取指定配置段指定变量值
#     :param env_vars: 环境变量集合，ChainMap类型，包含当前指定环境的环境变量、配置的全局变量、系统环境变量
#     :return:
#     """
#     my_log().info(f"Starting Class:{request.cls.__name__}")
#     env = request.config.getini("env")  # 读取ini文件中[pytest]配置段env的值
#     base_url = ini.get(env, 'base_url')  # 读取ini文件中env配置段base_url的值
#     print(f"\nbase_url: {base_url}")
#     for k, v in env_vars.items():  # 读取环境变量集合，包含当前指定环境的环境变量、配置的全局变量、系统环境变量
#         print(f"\n params: {k}={v}")
#     yield
#     my_log().info(f"Finished Class:{request.cls.__name__}")


@pytest.fixture(scope='function', autouse=True)
def function_fixture(request):
    my_log().info(f"Starting Function:{request.function.__name__}")
    yield
    my_log().info(f"Finished Function:{request.function.__name__}")


@pytest.fixture(scope='function', params=[1, 2, 3], ids=['one', 'two', 'three'])
def setup_method_fixture(request):
    my_log().info("\nself define setup method")
    return request.param
    # yield
    # my_log().info("self define teardown method")


@pytest.fixture(scope='function')
def setup_method_fixture_aa():
    my_log().info("\nself define setup method")
    yield
    my_log().info("\nself define teardown method")



