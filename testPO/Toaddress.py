from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Toaddress:
    def __init__(self,driver):
        self.driver = driver
    def toadd(self):
        def wait_name(driver):
            driver.find_element(By.XPATH, "//*[@class='ww_operationBar']/*[@class='qui_btn ww_btn js_add_member']").click()
            ele = driver.find_elements_by_xpath("//*[@placeholder='姓名']")
            return len(ele) > 0

        WebDriverWait(self.driver, 20).until(wait_name)
        # sleep(10)

        # self.driver.find_element_by_xpath("//*[@placeholder='姓名']").click()
        self.driver.find_element_by_xpath("//*[@placeholder='姓名']").send_keys('123134efds')

