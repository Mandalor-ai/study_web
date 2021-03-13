# 通讯录页
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from testapppo.apptwo.AddMan_Fun import AddMan_Fun
from testapppo.apptwo.base_page import BasePage


class AddressPage(BasePage):
    # 定义init方法接收上一个页面传过来的driver
    # def __init__(self, driver: webdriver):
    #     self.driver = driver

    def add_man(self):
        self.swipe_find("添加成员").click()
        return AddMan_Fun(self.driver)
