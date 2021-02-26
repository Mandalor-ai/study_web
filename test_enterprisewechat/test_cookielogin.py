from selenium import webdriver


class Test_cookie:
    def setup(self):
        self.driver= webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com')
    def teardown(self):
        pass

    def test_ck(self):
        self.driver.get_cookie()
