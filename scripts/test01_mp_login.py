from time import sleep
import pytest
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_log()


class TestMpLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_driver(page.mp_url)
        # 通过统一入口类获取PageMpLogin对象
        self.mp = PageIn(driver).page_get_PageMpLogin()

    # 结束
    def teardown_class(self):
        sleep(2)
        GetDriver.quit_driver()

    # 测试业务方法
    @pytest.mark.parametrize('username, pwd, expect, screenshot_name', read_yaml('mp_login.yml'))
    def test_mp_login(self, username, pwd, expect, screenshot_name):
        # 调用登录业务方法
        self.mp.page_my_login(username, pwd)
        try:
            # 断言
            assert expect == self.mp.page_get_nickname()
        except Exception as e:
            log.error('断言 登录失败, 失败信息: {}'.format(e))
            # print('错误原因:', e)
            # 截图
            self.mp.base_screenshot(screenshot_name)
            # 抛出异常
            raise
