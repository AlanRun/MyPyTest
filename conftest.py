import pytest

from common.yaml_util import clear_yaml
from logs.log_util import LogUtil


@pytest.fixture(scope='class', autouse=True)
def class_fixture(request):
    clear_yaml()
    LogUtil(request.cls.__name__).log_info(f"Starting Class:{request.cls.__name__}")
    yield
    LogUtil(request.cls.__name__).log_info(f"Finished Class:{request.cls.__name__}")


@pytest.fixture(scope='function', autouse=True)
def function_fixture(request):
    LogUtil(request.cls.__name__).log_info(f"Starting Function:{request.function.__name__}")
    yield
    LogUtil(request.cls.__name__).log_info(f"Finished Function:{request.function.__name__}")


@pytest.fixture(scope='function', params=[1, 2, 3], ids=['one', 'two', 'three'])
def setup_method_fixture(request):
    print("\nself define setup method")
    return request.param
    # yield
    # print("self define teardown method")


@pytest.fixture(scope='function')
def setup_method_fixture_aa():
    print("\nself define setup method")
    yield
    print("\nself define teardown method")
