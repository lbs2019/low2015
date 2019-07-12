# 导包
import unittest

# 新建测试类 继承
import requests
from parameterized import parameterized

from api.api_login import ApiLogin


def get_data():
    return [("13800001111", "123456", "8888", "登陆成功"),
            ("13800001112", "123456", "8888", "账号不存在!"),
            ("13800001111", "1234567", "8888", "密码错误!")]


class TestLogin(unittest.TestCase):
    session = None

    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取session
        cls.session = requests.session()
        # 实例化ApiLogin对象
        cls.login = ApiLogin(cls.session)

    # 结束
    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    # 测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, password, verify_code, expect):
        # 调用 验证码
        self.login.api_get_verify_code()
        # 调用 登录
        r = self.login.api_post_login(username, password, verify_code)
        print(r.json())
        # 断言
        self.assertEqual(expect, r.json().get("msg"))
