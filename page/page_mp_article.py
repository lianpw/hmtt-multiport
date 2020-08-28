from time import sleep
from base.web_base import WebBase
import page
from tools.get_log import GetLog

log = GetLog.get_log()


class PageMpArticle(WebBase):
    # 点击 内容管理
    def page_click_content_manager(self):
        sleep(1)
        self.base_click(page.login_content_manager)

    # 点击 发布文章
    def page_click_publish_article(self):
        sleep(1)
        self.base_click(page.login_publish_article)

    # 输入 标题
    def page_input_title(self, title):
        sleep(1)
        self.base_input(page.login_article_title, title)

    # 输入 内容
    def page_input_content(self, content):
        # 切换iframe
        iframe = self.base_find(page.login_iframe)
        self.driver.switch_to.frame(iframe)
        # 输入内容
        self.base_input(page.login_content, content)
        # 回到默认目录
        self.driver.switch_to.default_content()

    # 选择 封面
    def page_check_cover(self):
        sleep(1)
        self.base_click(page.login_cover)

    # 选择 频道
    def page_check_channel(self):
        # 调用webbase封装方法
        self.web_base_click_element('请选择', click_text='数据库')

    # 点击 发表按钮
    def page_click_submit(self):
        self.base_click(page.login_publish_btn)

    # 获取 发表提示信息
    def page_get_message(self):
        return self.base_get_text(page.login_result)

    # 组合发布文章业务方法
    def page_mp_article(self, title, content):
        log.info('正在调用自媒体组合发布文章业务方法, 标题为: {}, 内容为: {}'.format(title, content))
        self.page_click_content_manager()
        self.page_click_publish_article()
        self.page_input_title(title)
        self.page_input_content(content)
        self.page_check_cover()
        self.page_check_channel()
        self.page_click_submit()
