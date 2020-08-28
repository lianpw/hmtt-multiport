from time import sleep
from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog

log = GetLog.get_log()


class TestMisAudit:
    # 初始化
    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_driver(page.mis_url)
        # 2. 获取统一入口类
        page_in = PageIn(driver)
        # 3. 调用成功登录依赖方法
        page_in.page_get_PageMisLogin().page_mis_login_success()
        # 4. 获取PageMisAudit对象
        self.audit = page_in.page_get_PageMisAudit()

    # 结束
    def teardown_class(self):
        sleep(2)
        GetDriver.quit_driver()

    # 审核文章业务测试方法
    def test_mis_audit(self, title=page.title, value=page.channel):
        # 调用审核文章业务方法
        self.audit.page_mis_audit(title, value)
        try:
            # 断言
            assert self.audit.page_assert_audit()
        except Exception as e:
            # 日志
            log.error('断言审核文章业务失败, 失败原因为: {}'.format(e))
            # 截图
            self.audit.base_screenshot('mis_audit001')
            # 抛出错误
            raise
