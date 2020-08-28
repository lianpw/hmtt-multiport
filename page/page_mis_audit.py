from time import sleep
from base.web_base import WebBase
import page
from tools.get_log import GetLog

log = GetLog.get_log()


class PageMisAudit(WebBase):
    # 文章id
    article_id = None

    # 点击 信息管理
    def page_click_msg_manage(self):
        # 1. 暂停时间
        sleep(1)
        # 2. 点击信息管理
        self.base_click(page.mis_msg_manage)

    # 点击 内容审核
    def page_click_conent_audit(self):
        # 1. 暂停时间
        sleep(1)
        # 2. 点击内容审核
        self.base_click(page.mis_content_audit)

    # 输入 文章标题
    def page_input_article_title(self, title):
        self.base_input(page.mis_article_title, title)

    # 输入 频道
    def page_input_channel(self, value):
        self.base_input(page.mis_channel, value)

    # 选择 状态
    def page_check_status(self, placeholder_text='请选择状态', click_text='待审核'):
        self.web_base_click_element(placeholder_text, click_text)

    # 点击 查询按钮
    def page_click_find_btn(self):
        # 1. 点击查询按钮
        self.base_click(page.mis_find_btn)
        # 2. 暂停时间
        sleep(2)

    # 获取 文章id
    def page_get_article_id(self):
        return self.base_get_text(page.mis_article_id)

    # 点击 通过按钮
    def page_click_pass_btn(self):
        self.base_click(page.mis_pass)

    # 点击 确认按钮
    def page_click_confirm_btn(self):
        # 1. 暂停时间
        sleep(1)
        # 2. 点击确认
        self.base_click(page.mis_confirm)

    # 组合发布文章业务方法
    def page_mis_audit(self, title, value):
        log.info('正在调用组合发布文章业务方法, 标题为: {}, 频道为: {}'.format(title, value))
        self.page_click_msg_manage()
        self.page_click_conent_audit()
        self.page_input_article_title(title)
        self.page_input_channel(value)
        self.page_check_status()
        self.page_click_find_btn()
        self.article_id = self.page_get_article_id()
        print('获取的文章id为:', self.article_id)
        self.page_click_pass_btn()
        self.page_click_confirm_btn()

    # 组合断言业务操作方法
    def page_assert_audit(self):
        log.info('正在调用组合断言业务方法')
        # 1. 暂停时间
        sleep(3)
        # 2. 修改状态 -> 审核通过
        self.page_check_status(click_text='审核通过')
        # 3. 点击查询按钮
        self.page_click_find_btn()
        # 4. 判断当前页面是否存在指定元素 并 返回结果
        return self.web_base_element_is_exist(self.article_id)