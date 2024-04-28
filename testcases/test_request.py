import json

import allure
import pytest

from common.request_util import RequestUtil
from common.yaml_util import *


@allure.feature('Test Request')
class TestRequest:

    @pytest.mark.parametrize("args_name", read_testcase('test_request.yaml'))
    @allure.step('Request')
    def test_request(self, args_name):
        print(f"Testcase: {args_name}")
        req_data = args_name.pop('request', False)
        if req_data:
            res = RequestUtil().send_request(**req_data)
