from appium.webdriver.common.mobileby import MobileBy

from testapppo.apptwo.base_page import BasePage
from testapppo.apptwo.details import Details


class BaseInfo(BasePage):

    def go_details(self):
        self.find_click(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/iga"]')
        return  Details(self.driver)