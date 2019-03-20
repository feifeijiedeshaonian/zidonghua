from selenium import webdriver
from time import sleep
import sys
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\zhixin\login_zx')
from login__zhixin import LoginZhiXin
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\zhiyou\登录')
from login__zhiyou import LoginZhiYou


class LoginZhiYouGuanLi():

    def __init__(self, driver):
        self.driver = driver

    def login_zhiyou_guanli(self):
        sleep(1)
        # 进入项目管理端
        self.driver.find_element_by_xpath(".//div[@class = 'user-name']/button").click()
        sleep(1)
        c = self.driver.window_handles
        self.driver.switch_to_window(c[-1])
        

if __name__ == "__main__":
    driver = webdriver.Chrome()
    zhixin = LoginZhiXin(driver)
    zhiyou = LoginZhiYou(driver)
    zhiyou_guanli = LoginZhiYouGuanLi(driver)
    zhixin.login_zhixin("13820921009", "1111qqqq")
    sleep(1)
    zhiyou.login_zhiyou()
    sleep(1)
    zhiyou_guanli.login_zhiyou_guanli()