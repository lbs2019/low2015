# 导包
import unittest

from tool.HTMLTestRunner import HTMLTestRunner
# 定义测试套件
suite = unittest.defaultTestLoader.discover("./")
# 获取报告存储文件流 并实例化HTMLTestRunner 调用run
with open("../report/report.html","wb")as f:
    HTMLTestRunner(stream=f).run(suite)