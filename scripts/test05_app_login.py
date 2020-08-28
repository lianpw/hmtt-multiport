from time import sleep
from page.page_in import PageIn
from tools.get_driver import GetDriver


class TestAppLogin:
    # 1. 初始化
    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_app_driver()
        # 2. 通过统一入口类获取PageAppLogin对象
        self.login = PageIn(driver).page_get_PageAppLogin()

    # 2. 结束
    def teardown_class(self):
        GetDriver.quit_app_driver()

    # 3. app登录测试业务方法
    def test_app_login(self, phone='13812345678', code='246810'):
        self.login.page_app_login(phone, code)
        print('是否登录成功:', self.login.page_is_login_success())
