import json
from string import Template

import allure
import pytest

from common.request_util import RequestUtil
from common.yaml_util import read_testcase
from debug_talk import get_random_num


@allure.feature('Test Request')
class TestRequest:

    @pytest.mark.parametrize("args", read_testcase('test_request.yaml'))
    @pytest.mark.run(order=get_random_num(1, 1000))
    @allure.step('Request')
    def test_request(self, args, env_vars):
        req_data = args.pop('request', False)
        if req_data:
            # replace variables  with environment variables in pytest.ini
            template = Template(json.dumps(req_data))
            req_data = json.loads(template.safe_substitute(env_vars))

            res = RequestUtil().send_request(**req_data)
