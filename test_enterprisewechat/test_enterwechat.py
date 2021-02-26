import json
from time import sleep

import pytest
from selenium import webdriver


# remote登录企业微信
class Test_welogin:
    def setup(self):
        # 先cmd 输入 chrome -remote-debugging-port=9222
        # 打开企业微信扫码登录
        # 执行程序
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=chrome_options)
        self.driver = webdriver.Chrome()
        # self.driver.get('https://work.weixin.qq.com/')
        self.driver.implicitly_wait(5)

    def teardown(self):
        sleep(5)
        self.driver.quit()

    @pytest.mark.skip
    def test_register(self):
        self.driver.find_element_by_xpath('//*[@class="index_head_info_pCDownloadBtn"]').click()
        self.driver.find_element_by_id('corp_name').send_keys('字节跳动')
        self.driver.find_element_by_id('corp_industry').click()
        self.driver.find_element_by_xpath("//*[@data-name='IT服务']").click()
        self.driver.find_element_by_xpath("//*[@data-name='互联网和相关服务']").click()
        self.driver.find_element_by_id('corp_scale_btn').click()
        self.driver.find_element_by_xpath("//*[@data-value='2006']").click()

    @pytest.mark.skip
    def test_login(self):
        self.driver.find_element_by_xpath('//*[@class="index_top_operation_loginBtn"]').click()
        self.driver.find_element_by_id('menu_apps').click()

        # 通过options获取cookie  存储在tmp.txt
        # def test_ck(self):
        #     cookies = self.driver.get_cookies()
        #     with open('tmp.txt','w', encoding='utf-8') as f:
        #         f.write(json.dumps(cookies))

    def test_cookielogin(self):
        self.driver.get('https://work.weixin.qq.com/')
        #读取本地文件保存的cookie
        with open('tmp.txt','r',encoding='utf-8') as f:
            cookies = json.loads(f.read())
            for i in cookies:
                self.driver.add_cookie(i)
            self.driver.refresh()
            sleep(2)
        self.driver.find_element_by_xpath('//*[@class="index_top_operation_loginBtn"]').click()
        self.driver.find_element_by_id('menu_apps').click()
