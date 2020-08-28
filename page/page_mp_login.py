from time import sleep
import page
from base.web_base import WebBase
from tools.get_log import GetLog

log = GetLog.get_log()


class PageMpLogin(WebBase):
    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_password(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取昵称 -> 测试脚本层断言使用
    def page_get_nickname(self):
        return self.base_get_text(page.login_nickname)

    # 业务组合方法 -> 测试脚本层调用
    def page_my_login(self, username, pwd):
        log.info('正在调用自媒体登录业务方法, 用户名: {}, 密码: {}'.format(username, pwd))
        self.page_input_username(username)
        self.page_input_password(pwd)
        sleep(1)
        self.page_click_login_btn()

    # 业务组合方法 -> 发布文章依赖使用
    def page_my_login_success(self, username='13812345678', pwd='246810'):
        log.info('正在调用自媒体登录依赖方法, 用户名: {}, 密码: {}'.format(username, pwd))
        self.page_input_username(username)
        self.page_input_password(pwd)
        sleep(1)
        self.page_click_login_btn()
