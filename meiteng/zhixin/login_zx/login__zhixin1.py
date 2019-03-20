from selenium import webdriver
from time import sleep
from selenium. webdriver. common. by import By
import sys
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\tongyong')
from common1 import Base
import logging
import time


class LoginZhiXin():

    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def get_windows_img(self):
        self.logger = logging.getLogger(__name__)
        file_path = 'E:\\screenshot\\'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        print(screen_name)
        try:
            self.driver.get_screenshot_as_file(screen_name)
            self.logger.info("Had take screenshot and save to folder : /creenshot")
        except NameError as e:
            self.logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    def login_zhixin(self, user="17694804822", psw="rsl123456"):
        # 输入网址
        self.driver.get("http://192.168.5.54/")
        sleep(1)
        # 输入账号密码
        loc1 = (By.XPATH, '//*[@id="mobile"]/input')
        loc2 = (By.XPATH, '//*[@id="password"]/input')
        loc3 = (By.ID, "loginBtn")
        self.driver.find_element_by_xpath('//*[@id="mobile"]/input').clear()
        Base.sendKeys(self, loc1, user, self.driver)
        Base.sendKeys(self, loc2, psw, self.driver)
        # self.get_windows_img()
        # 点击登陆
        Base.click(self, loc3, self.driver)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    zhixin = LoginZhiXin(driver)
    zhixin.login_zhixin("13820921009", "1111qqqq")






def findElementByID(driver, element_id, n=10, sleeptime=1):
    for i in range(n):
        try:
            ret = driver.find_element_by_id(element_id)
            return ret
        except Exception:
            print(u'loading:' + element_id)
            time.sleep(sleeptime)
            if i == n-1:
                print("loading fail:" + element_id)
    raise Exception("element %s could not be found" % element_id)