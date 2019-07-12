"""
    目标：mock简单实用
"""
# 导包
# from unittest import mock
from unittest.mock import Mock
import unittest


# 未实现功能 对象/函数
def add(a,b):
    # 暂时未实现
    pass


class TestAdd(unittest.TestCase):

    def test_add(self):
        # 获取Mock对象，并设置它的行为 且 替换未完成的对象或函数
        add = Mock(return_value=20)
        result = add(10,10)
        print(result)

    # 扩展：模拟抛出异常
    def test_error(self):
        # 获取Mock对象，并设置它的行为 且 替换未完成的对象或函数
        add = Mock(return_value=NameError("对不起，XXX文件未找到"))
        result = add(10,10)
        print(result)