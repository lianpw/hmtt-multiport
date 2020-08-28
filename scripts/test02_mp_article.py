from time import sleep
import pytest
from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog().get_log()


class TestMpArticle:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_driver(page.mp_url)
        # 获取统一入口类对象
        self.page_in = PageIn(driver)
        # 获取PageMpLogin对象并调用成功登录依赖方法
        self.page_in.page_get_PageMpLogin().page_my_login_success()
        # 获取PageMpArticle页面对象
        self.article = self.page_in.page_get_PageMpArticle()

    # 结束
    def teardown_class(self):
        sleep(2)
        GetDriver.quit_driver()

    # 测试发布文章业务方法
    @pytest.mark.parametrize('title, content, expect, screenshot_name, channel', read_yaml('mp_article.yaml'))
    def test_mp_article(self, title, content, expect, screenshot_name):
        # 调用发布文章业务方法
        self.article.page_mp_article(title, content)
        try:
            assert expect == self.article.page_get_message()
            print(self.article.page_get_message())
        except Exception as e:
            log.error('断言 发布文章失败, 失败信息为: {}'.format(e))
            # print('错误原因:', e)
            # 截图
            self.article.base_screenshot(screenshot_name)
            # 抛出异常
            raise
