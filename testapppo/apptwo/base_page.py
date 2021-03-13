


# 封装就是把重复的代码提取出来
from _pytest import logging
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    # #定义在基类里面定义init方法  使其他类继承基类  webdriver = None  初始化变量
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 封装find_element(Byid,'值')方法
    def find(self, locator, value):
        return self.driver.find_element(locator, value)

    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    def find_click(self, locator, value):
        return self.driver.find_element(locator, value).click()

    def find_sends(self, locator, value,value2):

        return self.driver.find_element(locator, value).send_keys(value2)

    def swipe_find(self, text, num=3):
        for i in range(num):
            if i == num - 1:
                self.driver.implicitly_wait(50)
                raise NoSuchElementException(f"找到{num}次， 未找到。")

            self.driver.implicitly_wait(10)
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(50)
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get("height")

                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.3

                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

