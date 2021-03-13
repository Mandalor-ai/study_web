import pytest
from appium.webdriver.common.mobileby import MobileBy

from testapppo.apptwo.app import App
from testapppo.apptwo.base_page import BasePage


class TestAppPo():

    def setup(self):
        # 完成driver初始化实现driver传递
        self.app = App().start_app()
        # 到首页
        self.main = self.app.go_main()

    def teardown(self):
        self.app.close_app()
    # self.app.close_app()
#添加联系人
    @pytest.mark.skip
    def test_a(self):
        # 一直页面跳转 先点击通讯录-点击添加联系人-选择联系方式-输入联系人+保存
        self.editpage = self.main.go_address().add_man().add_man_method()
        self.editpage.edit_man()
        # 校验添加是否成功
        self.editpage.verify_ok()
#删除联系人
    def test_delman(self):
        name ='hgws03'
        delpage = self.main.search_man(name).go_details().edit_man()
        delpage.del_man_operation()
        delpage.is_true(name)

