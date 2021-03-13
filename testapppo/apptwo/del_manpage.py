from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from testapppo.apptwo.base_page import BasePage


class DelManPage(BasePage):
    def del_man_operation(self):
        self.swipe_find('删除成员').click()
        self.find_click(MobileBy.XPATH, '//*[@text="删除成员"]')
        self.find_click(MobileBy.XPATH, '//*[@text="确定"]')
    def is_true(self,name):
        sleep(5)
        elements_man = self.finds(MobileBy.XPATH,f'//*[@text="{name}"]')
        print(len(elements_man))
        if len(elements_man)<=1:
           assert '删除成功'
        else:
           assert '删除失败'

