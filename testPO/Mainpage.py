from time import sleep

from selenium import webdriver

from testPO.Toaddress import Toaddress


class Mainpage:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
    def mainpage(self):
        self.driver.find_element_by_id('menu_contacts').click()
        sleep(3)
        return Toaddress(self.driver)