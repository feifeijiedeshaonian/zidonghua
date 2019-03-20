from selenium import webdriver
from time import sleep
from selenium. webdriver. common. by import By
import sys
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\zhixin\login_zx')
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\tongyong')
from login__zhixin1 import LoginZhiXin
from common1 import Base


class LoginZhiYou():

    def __init__(self, driver):
        self.driver = driver

    def login_zhiyou(self):
        
        sleep(2)
        loc1 = (By.XPATH, '//*[@id="app"]/div/aside/ul/li[3]/button')  
        Base.click(self, loc1, self.driver)
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



    # loc1 = (By.XPATH, '//*[@id="mobile"]/input')
    #     loc2 = (By.XPATH, '//*[@id="password"]/input')
    #     loc3 = (By.ID, "loginBtn")
    #     Base.sendKeys(self, loc1, user, self.driver)
    #     Base.sendKeys(self, loc2, psw, self.driver)
    #     # 点击登陆
    #     Base.click(self, loc3, self.driver)