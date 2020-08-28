import os
import allure
from selenium.webdriver.support.wait import WebDriverWait
from config import BASE_PATH
from tools.get_log import GetLog

log = GetLog.get_log()


class Base:

    # 初始化
    def __init__(self, driver):
        log.info('正在初始化driver: {}'.format(driver))
        self.driver = driver

    # 查找方法
    def base_find(self, loc, timeout=30, poll=0.5):
        log.info('正在查找元素: {}'.format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 输入方法
    def base_input(self, loc, value):
        print('loc为:', loc)
        el = self.base_find(loc)
        log.info('正在对: {}元素执行清空操作!'.format(loc))
        el.clear()
        log.info('正在对: {}元素执行输入: {}操作!'.format(loc, value))
        print('value值为:', value)
        el.send_keys(value)

    # 点击方法
    def base_click(self, loc):
        log.info('正在对: {}元素执行点击操作!'.format(loc))
        self.base_find(loc).click()

    # 获取元素文本
    def base_get_text(self, loc):
        log.info('正在对: {}元素获取文本操作! 获取文本值: {}'.format(loc, self.base_find(loc).text))
        return self.base_find(loc).text

    # 截图方法
    def base_screenshot(self, filename):
        filepath = BASE_PATH + os.sep + 'screenshot' + os.sep + filename + '.png'
        log.error('断言出错, 正在执行截图操作!')
        self.driver.get_screenshot_as_file(filepath)

        # 调用图片写入报告方法
        log.error('断言错误, 正在将图片写入allure报告!')
        self.__base_write_img(filename)

    # 将图片写入报告方法 (私有方法)
    def __base_write_img(self, filename):
        filepath = BASE_PATH + os.sep + 'screenshot' + os.sep + filename + '.png'
        # 获取图片写入文件流
        with open(filepath, 'rb') as f:
            allure.attach(f.read(), '错误原因:', allure.attachment_type.PNG)
