import re

import allure
import requests
import jsonpath
from common.yaml_util import write_yaml


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
        method = str(kwargs.pop('method', 'GET')).lower()
        url = kwargs.pop('url', None)
        data = kwargs.pop('data', None)
        params = kwargs.pop('params', None)
        json = kwargs.pop('json', None)
        headers = kwargs.pop('headers', None)
        cookies = kwargs.pop('cookies', None)
        files = kwargs.pop('files', None)
        timeout = kwargs.pop('timeout', None)
        allow_redirects = kwargs.pop('allow_redirects', False)
        proxies = kwargs.pop('proxies', None)
        hooks = kwargs.pop('hooks', None)
        stream = kwargs.pop('stream', None)
        verify = kwargs.pop('verify', None)
        cert = kwargs.pop('cert', None)
        res = RequestUtil.sess.request(method=method, url=url, json=json, params=params, data=data, headers=headers,
                                       cookies=cookies, files=files, timeout=timeout, allow_redirects=allow_redirects,
                                       proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert)

        # verify the response
        self.verify_response(res, kwargs.pop('response', None))

        # extract the data from the response
        self.extract_data(res, kwargs.pop('extract', None))

        # validate the response
        self.validate_response(res, kwargs.pop('validate', None))

        # return the response
        return res

    @allure.step("Verify response")
    def verify_response(self, res, res_expected):
        assert res.status_code == res_expected.pop('status_code', None)

    @allure.step("Extract data form response")
    def extract_data(self, res, extract):
        if extract:
            for k, p in extract.items():
                # 正则表达式格式提取
                # re.search('url":"(.*?)"', res.text)

                # jsonpath格式提取
                v = jsonpath.jsonpath(res.json(), p)[0]
                write_yaml({k: v})

    @allure.step("Validate response")
    def validate_response(self, res, validate):
        if validate and 'application/json' in res.headers['Content-Type']:
            for item in validate:
                for k, v in item.items():
                    if k == 'eq':
                        for key, value in v.items():
                            actual = jsonpath.jsonpath(res.json(), key)[0]
                            assert actual == value
                    elif k == 'contains':
                        for key, value in v.items():
                            actual = jsonpath.jsonpath(res.json(), key)[0]
                            assert value in actual
