#进入添加成员方式页面
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from testapppo.apptwo.Add_Edit_Main import Add_Edit_Main
from testapppo.apptwo.base_page import BasePage


class AddMan_Fun(BasePage):
    # def __init__(self, driver: webdriver):
    #     self.driver = driver
    #选择添加成员方式
    def add_man_method(self):
        self.find_click(MobileBy.XPATH, '//*[@text="手动输入添加"]')
        return Add_Edit_Main(self.driver)
