from appium import webdriver

import yaml
# 第一步  创建app的操作类
# 启动 重启 关闭  页面跳转
from testapppo.apptwo.MainPage import MainPage
from testapppo.apptwo.base_page import BasePage

# with open('C:/Users/Admin/PycharmProjects/study_web/testapppo/apptwo/caps.yml') as f:
with open('./data/caps.yml') as f:
    datas = yaml.safe_load(f)
    desires = datas['desirecaps']
    ip = datas['server']['ip']
    port = datas['server']['port']
class App(BasePage):
    # 启动app
    def start_app(self):
        if self.driver == None:
            # caps = {}
            # caps["platformName"] = "android"
            # caps["deviceName"] = "127.0.0.1:7555"
            # caps["appPackage"] = "com.tencent.wework"
            # caps["appActivity"] = ".launch.LaunchSplashActivity"
            # caps["noReset"] = "true"
            # caps['settings[waitForIdleTimeout]'] = 1
            # caps["unicodeKeyboard"] = True
            # caps["resetKeyboard"] = True
            # caps['skipServerInstallation'] = "true"
            # # 跳过设备的初始化
            # caps['skipDeviceInitialization'] = "true"
            # # 运行前不停止app
            # caps['dontStopAppOnReset'] = "true"
            self.driver = webdriver.Remote(f'http://{ip}:{port}/wd/hub', desires)
            self.driver.implicitly_wait(50)
        else:
            self.driver.launch_app()
        return self
    # 关闭app
    def close_app(self):
        # self.driver.quit()
        pass
    # 重启app
    def restart_app(self):
        self.driver.close_app()
        self.driver.launch_app()

    # 到app的首页
    def go_main(self):
        #要把启动的driver传入下一个页面
        return MainPage(self.driver)
