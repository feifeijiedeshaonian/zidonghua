from selenium import webdriver
from time import sleep


class LoginZhiXin():
    
    def __init__(self, driver):
        self.driver = driver
        # 窗口最大化
        driver.maximize_window()

    def login_zhixin(self, user="17694804822", psw="rsl123456"):
        # 输入网址
        self.driver.get("http://192.168.5.54/")
        sleep(1)
        # 输入账号密码
        self.driver.find_element_by_xpath('//*[@id="mobile"]/input').send_keys(user)
        self.driver.find_element_by_xpath('//*[@id="password"]/input').send_keys(psw)
        # 点击登陆
        self.driver.find_element_by_id("loginBtn").click()
        

if __name__ == "__main__":
    driver = webdriver.Chrome()
    zhixin = LoginZhiXin(driver)
    zhixin.login_zhixin("13820921009", "1111qqqq")
    driver.get_screenshot_as_file("E:\\screenshot\\denglu.png")