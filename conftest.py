"""
This file is used to define fixtures for the test cases.
"""
import pytest

from common.yaml_util import clear_yaml
from common.log_util import my_log


@pytest.fixture(scope='class', autouse=True)
def class_fixture(request):
    clear_yaml()
    my_log().info(f"Starting Class:{request.cls.__name__}")
    yield
    my_log().info(f"Finished Class:{request.cls.__name__}")


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
