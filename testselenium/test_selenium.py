from time import sleep

import selenium
import pytest
from selenium import webdriver


class TestA:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        # self.driver.get('https://www.baidu.com/')

        self.driver.get('https://www.testing-studio.com')
    def teardown(self):
        sleep(5)
        # self.driver.quit()

    def test_a(self):
        # self.driver.find_element_by_id('kw').send_keys('aaa')
        # self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('霍格沃兹测试学院')
        # self.driver.find_element_by_id('su').click()
        # self.driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
        # self.driver.find_element_by_css_selector('#menu-item-211>a').click()
        self.driver.find_element_by_xpath('//*[@id="menu-item-927"]/a').click()
        # self.driver.execute_script('document.getElementById("menu-item-211")')
