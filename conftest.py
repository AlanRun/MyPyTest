import pytest

from common.yaml_util import clear_yaml


@pytest.fixture(scope='class', autouse=True)
def teardown_class_fixture():
    clear_yaml()
    yield
    print('\nself define teardown class')


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
