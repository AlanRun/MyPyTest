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
        self.validate_response(res, kwargs.get('validate', None))

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
        assert res.status_code == res_expected.get('status_code', None)

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
                # 正则表达式格式提取
                # re.search('url":"(.*?)"', res.text)

                # jsonpath格式提取
                v = jsonpath.jsonpath(res.json(), p)[0]
                write_yaml({k: v})

    @allure.step("Validate response")
    def validate_response(self, res, validate):
        """
        This method is used to validate the response of the API.
        :param res:
        :param validate:
        :return:
        """
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
