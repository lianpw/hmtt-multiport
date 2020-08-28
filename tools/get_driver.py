from time import sleep
from selenium import webdriver
import appium.webdriver
import page


class GetDriver:
    # 1. 声明变量
    __driver = None

    __app_driver = None

    # 2. 获取driver方法
    @classmethod
    def get_driver(cls, url):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            cls.__driver.get(url)
        return cls.__driver

    # 3. 退出driver方法
    @classmethod
    def quit_driver(cls):
        if cls.__driver:
            cls.__driver.quit()
            cls.__driver = None

    # 获取app应用driver
    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            # 设置启动
            desired_caps = {}
            # 设备信息
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '8.0'
            desired_caps['deviceName'] = '192.168.56.101:5555'
            # app的信息
            desired_caps['appPackage'] = page.appPackage
            desired_caps['appActivity'] = page.appActivity
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True
            # desired_caps['automationName'] = 'Uiautomator2'
            # 设置driver
            cls.__app_driver = appium.webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return cls.__app_driver

    # 退出app应用driver
    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver:
            cls.__app_driver.quit()
            cls.__app_driver = None


if __name__ == '__main__':
    GetDriver.get_app_driver()
    sleep(2)
    GetDriver.quit_app_driver()
