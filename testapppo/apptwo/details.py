from appium.webdriver.common.mobileby import MobileBy

from testapppo.apptwo.base_page import BasePage
from testapppo.apptwo.del_manpage import DelManPage


class Details(BasePage):
    def edit_man(self):
        self.find_click(MobileBy.XPATH, '//*[@text="编辑成员"]')
        return DelManPage(self.driver)