import sys
from time import sleep

import pytest
from selenium.webdriver import ActionChains

from testselenium.base import Base


class Test_ac(Base):
    @pytest.mark.skip
    def test_baidu(self):
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('霍格沃兹测试学院')
        ele = self.driver.find_element_by_xpath('//*[@id="kw"]')
        action = ActionChains(self.driver)
        # 右键
        action.context_click(ele)
        # 双击鼠标左键
        action.double_click(ele)
        action.perform()

    @pytest.mark.skip
    def test_shubiaoyidong(self):
        ele_mousemove = self.driver.find_element_by_css_selector('#s-usersetting-top')
        action = ActionChains(self.driver)
        #鼠标移动至
        action.move_to_element(ele_mousemove)
        action.perform()
    @pytest.mark.skip
    def test_drag_to_drop(self):
        # self.driver.switch_to_frame('iframeResult')
        # for i in range(10):
        #     self.driver.find_element_by_css_selector('body > pre > p').click()
        #切换到iframe
        self.driver.switch_to_frame('iframeResult')
        drag_a = self.driver.find_element_by_css_selector('#draggable')
        drop_b = self.driver.find_element_by_css_selector('#droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_a,drop_b)
        action.perform()
        sleep(2)
        #切换出iframe
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_css_selector('#submitBTN > span').click()
    def test_window_qiehuan(self):
        self.driver.find_element_by_css_selector('#u1 > a').click()
        self.driver.find_element_by_link_text('立即注册').click()
        a = self.driver.window_handles
        self.driver.switch_to.window(a[1])
        self.driver.find_element_by_name('userName').send_keys('zhangshuchaohaoshuai')
        self.driver.find_element_by_name('phone').send_keys('16619929565')
        self.driver.switch_to.window(a[0])
