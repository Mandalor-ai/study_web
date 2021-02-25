from time import sleep

from selenium import webdriver


class Base:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com/')

        # self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-drop-effect')
        # self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-example-droppable')
    def teardown(self):
        sleep(5)
        # self.driver.quit()