class ApiLogin:
    # 初始化
    def __init__(self, session):
        self.session = session

    # 请求验证码
    def api_get_verify_code(self):
        # 定义url
        url = "http://www.tpshop.com/index.php?m=Home&c=User&a=verify"
        self.session.get(url)

    # 登录
    def api_post_login(self, username, password, verify_code):
        url = "http://www.tpshop.com/index.php?m=Home&c=User&a=do_login"
        data = {"username": username, "password": password, "verify_code": verify_code}
        # 在业务成要使用断言，必须return返回响应对象
        return self.session.post(url, data=data)
