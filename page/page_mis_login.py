from time import sleep

from base.web_base import WebBase
import page
from tools.get_log import GetLog

log = GetLog.get_log()


class PageMisLogin(WebBase):
    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.mis_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.mis_pwd, pwd)

    # 点击登录按钮
    def page_click_login_btn(self):
        # 处理js
        js = "document.getElementById('inp1').disabled = false"
        self.driver.execute_script(js)
        # 调用点击操作
        self.base_click(page.mis_login_btn)
        sleep(1)

    # 获取昵称
    def page_get_nickname(self):
        return self.base_get_text(page.mis_nickname)

    # 组合后台管理登录业务方法
    def page_mis_login(self, username, pwd):
        log.info('正在调用后台管理系统登录业务方法, 用户名为: {}, 密码为: {}'.format(username, pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    # 组合后台管理登录业务方法 -> 审核文章依赖使用
    def page_mis_login_success(self, username='testid', pwd='testpwd123'):
        log.info('正在调用后台管理系统登录依赖方法, 用户名为: {}, 密码为: {}'.format(username, pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
