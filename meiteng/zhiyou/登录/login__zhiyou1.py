from selenium import webdriver
import sys
from time import sleep
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\zhixin\login_zx')
from login__zhixin1 import LoginZhiXin


class LoginZhiYou():

    def __init__(self, driver):
        self.driver = driver

    def login_zhiyou(self):
        
        sleep(2)  
        self.driver.find_element_by_xpath('//*[@id="app"]/div/aside/ul/li[3]/button').click()
        # 切换光标定位
        a = self.driver.current_window_handle
        b = self.driver.window_handles
        self.driver.switch_to_window(b[-1])
        sleep(1)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    zhixin = LoginZhiXin(driver)
    zhiyou = LoginZhiYou(driver)
    zhixin.login_zhixin("13820921009", "1111qqqq")
    sleep(1)
    zhiyou.login_zhiyou()