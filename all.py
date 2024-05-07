import os

import pytest

"""
-s:表示输出调试信息，包括print打印的信息
-v:显示更详细的信息
-vs : 这两个参数一起用
-n: 支持多线程或者分布式运行测试用例。如 : pytest -vs ./testcase/test login.py -n 2--reruns NUM :失败用例重跑
-x : 表示只要要一个用例报错，那么测试停止--maxfail=2 出现两个用例失败就停止。
-k:根据测试用例的部分字符串指定测试用例如 : pytest -vs ./testcase -k "ao"
pdb.set_trace()断点
执行顺序：@pytest.mark.run(order=1)
参数化： @pytest.mark.parametrize("num, expected", data1)
--random-order : 随机执行用例
"""
if __name__ == '__main__':
    # pytest.main(['-vs', 'test_1.py::TestDemo::test_aa', '-n=2', '--reruns=2'])
    pytest.main(['-vs', './testcases/test_request.py'])
    os.system("allure generate ./temp/ -o ./reports --clean")
