from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class Test_demo:

    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps['settings[waitForIdleTimeout]'] = 1
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(50)

    def teardown(self):
        pass
    @pytest.mark.skip
    def test_a(self):
        # 定位并点击工作台
        self.driver.find_element(MobileBy.XPATH, '//*[@text="工作台"]').click()
        # 固定方法 滑动页面，加载出打卡的元素  里面一定要是双引号  java语法
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        # 定位 //*[@text='外出打卡']  并点击
        self.driver.find_element(MobileBy.XPATH, '//*[@text="外出打卡"]').click()
        # 定位不变元素 //*[contains(@text,"次外出")] contains() 方法
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"次外出")]').click()
        #获取文件源码
        #通过查找元素触发隐式等待 完成所需元素加载
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")
        assert  '外出打卡' in self.driver.page_source
    '''
    案例：作业
        1，点击通讯录
        2，点击添加成员
        3，点击手动输入添加
        3.1 点击更多选项
        4，定位姓名，输入‘张无忌’
        4.1 定位别名输入‘教主’
        5，定位手机号，输入‘18515156179’
        6，点击性别，定位女并点击
        7，点击地址，跳转到另一页面
        8，定位输入框输入海淀
        9，定位第一条海淀黄庄【地铁站】 并点击
        10，定位确定按钮，并点击
        11，点击保存
        12.返回首页
    '''
    def test_contacts(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="更多选项"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="必填"]').send_keys('赵敏')
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"别名")]/../android.widget.EditText').send_keys('教主')
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手机号"]').send_keys('18515156079')
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"邮箱")]/../android.widget.EditText').send_keys('592545895@qq.com')
        self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'地址')]/..//*[@text='选填']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'请输入')]").send_keys('haidian')
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'海淀黄庄[地铁站]')]").click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="确定"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        self.driver.keyevent(4)



