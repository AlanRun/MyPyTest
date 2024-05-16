import re

import allure
import requests
import jsonpath

from common.assert_util import AssertUtil
from common.yaml_util import write_yaml, is_json


class RequestUtil:
    """
    This class is used to handle the request and response of the API.
    """

    sess = requests.session()

    @allure.step("Send request")
    def send_request(self, **kwargs):
        """
        This method is used to send the request to the API.
        :param kwargs:
        :return:
        """
        method = str(kwargs.get('method', 'GET')).lower()
        url = kwargs.get('url', None)
        data = kwargs.get('data', None)
        params = kwargs.get('params', None)
        json = kwargs.get('json', None)
        headers = kwargs.get('headers', None)
        cookies = kwargs.get('cookies', None)
        files = kwargs.get('files', None)
        timeout = kwargs.get('timeout', None)
        allow_redirects = kwargs.get('allow_redirects', False)
        proxies = kwargs.get('proxies', None)
        hooks = kwargs.get('hooks', None)
        stream = kwargs.get('stream', None)
        verify = kwargs.get('verify', None)
        cert = kwargs.get('cert', None)
        res = RequestUtil.sess.request(method=method, url=url, json=json, params=params, data=data, headers=headers,
                                       cookies=cookies, files=files, timeout=timeout, allow_redirects=allow_redirects,
                                       proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert)

        # verify the response
        self.verify_response(res, kwargs.get('response', None))

        # extract the data from the response
        self.extract_data(res, kwargs.get('extract', None))

        # validate the response
        self.validate_response_body(res, kwargs.get('validate', None))

        # return the response
        return res

    @allure.step("Verify response")
    def verify_response(self, res, res_expected):
        """
        This method is used to verify the response of the API.
        :param res:
        :param res_expected:
        :return:
        """
        AssertUtil().equal_to(res_expected.get('status_code', None), res.status_code)

    @allure.step("Extract data form response")
    def extract_data(self, res, extract):
        """
        This method is used to extract the data from the response of the API.
        :param res:
        :param extract:
        :return:
        """
        if extract:
            for k, p in extract.items():
                if r'$.' in p:
                    # jsonpath格式提取
                    try:
                        v = jsonpath.jsonpath(res.json(), p)[0]
                    except TypeError:
                        v = None
                else:
                    # 正则表达式格式提取
                    v = re.search(p, res.text).group(1)
                write_yaml({k: v})

    @allure.step("Validate response body")
    def validate_response_body(self, res, validate):
        """
        This method is used to validate the response of the API.
        :param res:
        :param validate:
        :return:
        """
        if validate and ('json' in res.headers['Content-Type'] or is_json(res.text)):
            for item in validate:
                for k, v in item.items():
                    if k == 'eq':
                        for key, value in v.items():
                            try:
                                actual = jsonpath.jsonpath(res.json(), key)[0]
                            except TypeError:
                                actual = ''
                            AssertUtil().equal_to(value, actual)
                    elif k == 'contains':
                        for key, value in v.items():
                            try:
                                actual = jsonpath.jsonpath(res.json(), key)[0]
                            except TypeError:
                                actual = ''
                            AssertUtil().is_in(value, actual)
