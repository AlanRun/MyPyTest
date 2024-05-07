
import pytest

from common.request_util import RequestUtil
from common.yaml_util import *
from debug_talk import DebugTalk


@allure.feature('Test Request')
class TestRequest:

    @pytest.mark.parametrize("args_name", read_testcase('test_request.yaml'))
    @pytest.mark.run(order=DebugTalk().get_random_num(1, 1000))
    @allure.step('Request')
    def test_request(self, args_name):
        args = json.dumps(args_name)
        print(f"\nTestcase: {args}")
        req_data = args_name.pop('request', False)

        if req_data:
            res = RequestUtil().send_request(**req_data)
