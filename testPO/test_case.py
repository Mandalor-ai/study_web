import json
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Test_case1:

    def test_case1(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('menu_contacts').click()

        sleep(3)

        def wait_name(driver):
            driver.find_element(By.XPATH, "//*[@class='ww_operationBar']/*[@class='qui_btn ww_btn js_add_member']").click()
            ele = driver.find_elements_by_xpath("//*[@placeholder='姓名']")
            return len(ele) > 0

        WebDriverWait(self.driver, 20).until(wait_name)
        # sleep(10)

        # self.driver.find_element_by_xpath("//*[@placeholder='姓名']").click()
        self.driver.find_element_by_xpath("//*[@placeholder='姓名']").send_keys('123134efds')
