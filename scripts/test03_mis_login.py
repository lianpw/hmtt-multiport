from time import sleep

import pytest

from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_log()


class TestMisLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_driver(page.mis_url)
        # 通过统一入口类获取PageMisLogin对象
        self.login = PageIn(driver).page_get_PageMisLogin()

    # 结束
    def teardown_class(self):
        sleep(2)
        GetDriver.quit_driver()

    # 登录测试业务方法
    @pytest.mark.parametrize('username, pwd, expect, screenshot_name', read_yaml('mis_login.yaml'))
    def test_mis_login(self, username, pwd, expect, screenshot_name):
        # 调用登录业务方法
        self.login.page_mis_login(username, pwd)
        try:
            # 调试断言信息
            assert expect in self.login.page_get_nickname()
        except Exception as e:
            log.error('断言 登录失败, 失败原因为: {}'.format(e))
            # 截图
            self.login.base_screenshot(screenshot_name)
            # 抛出异常
            raise
