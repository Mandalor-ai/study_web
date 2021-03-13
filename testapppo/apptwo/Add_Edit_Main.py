# 进入联系人编辑页面
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from testapppo.apptwo.base_page import BasePage


class Add_Edit_Main(BasePage):
    # def __init__(self, driver: webdriver):
    #     self.driver = driver
    # 编辑联系人
    def edit_man(self):
        name = 'hgws06'
        phonecode = '13589599752'
        self.find_sends(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText",name)
        self.find_sends(MobileBy.XPATH, "//*[contains(@text,'手机')]/../android.widget.EditText",phonecode)
        self.find_click(MobileBy.XPATH, '//*[@text="设置部门"]')
        self.find_click(MobileBy.XPATH, '//*[@text="确定(1)"]')
        self.find_click(MobileBy.XPATH, '//*[@text="保存"]')
    # 确认是否添加成功
    def verify_ok(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成功"]')
