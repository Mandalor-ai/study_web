#app首页
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from testapppo.apptwo.AddressPage import AddressPage
from testapppo.apptwo.base_info import BaseInfo
from testapppo.apptwo.base_page import BasePage


class MainPage(BasePage):
    # #定义init方法接收上一个页面传过来的driver  driver:webdriver  定义driver类型，在本页面可以有代码提示
    # def __init__(self,driver:webdriver):
    #     self.driver = driver
    #进入通讯录页面

    def go_address(self):
        #定位通讯录按钮并点击 ，进入通讯录页
        # self.driver(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.find_click(MobileBy.XPATH, '//*[@text="通讯录"]')
        return AddressPage(self.driver)
    def search_man(self,name):
        self.find_click(MobileBy.XPATH, '//*[@text="通讯录"]')
        self.find_click(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/igk"]')
        # 输入搜索条件

        self.find_sends(MobileBy.XPATH, '//*[@text="搜索"]',name)
        # 判断是否存在
        sleep(5)
        elements = self.finds(MobileBy.XPATH,f'//*[@text="{name}"]')
        if len(elements) > 1:
            elements[1].click()
            return BaseInfo(self.driver)
        else:
            print(len(elements))
            self.driver.keyevent(4)
            print('不存在用户')


