from time import sleep
from selenium.webdriver.common.by import By
from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_log()


class WebBase(Base):
    """以下为web项目专属方法"""
    # 根据显示文本点击指定元素
    def web_base_click_element(self, placeholder_text, click_text):
        # 点击下拉选择框
        loc = By.CSS_SELECTOR, "[placeholder='{}']".format(placeholder_text)
        log.info('正在对下拉框元素: {}执行点击操作'.format(loc))
        self.base_click(loc)
        # 暂停
        sleep(1)
        # 点击指定文本元素
        loc = By.XPATH, "//*[text()='{}']".format(click_text)
        log.info('正在对元素: {} 执行点击操作'.format(loc))
        self.base_click(loc)

    # 判断页面是否包含指定元素
    def web_base_element_is_exist(self, text):
        log.info('正在查找页面中是否存在元素: {}'.format(text))
        # 1.组装元素配置信息
        loc = By.XPATH, "//*[text()='{}']".format(text)
        # 2. 找元素
        try:
            self.base_find(loc, timeout=3)
            print('找到: {}元素信息了!'.format(loc))
            return True
        except:
            print('没有找到: {}元素信息!'.format(loc))
            return False
