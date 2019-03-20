from selenium import webdriver
from time import sleep
import sys
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\zhixin\login_zx')
from login__zhixin import LoginZhiXin
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\zhiyou\登录')
from login__zhiyou import LoginZhiYou


class CreateTemporaryProject():

    def __init__(self, driver):
        self.driver = driver

    def create_temporary_project(self, name):
        # 点击临时项目
        self.driver.find_element_by_xpath('//*[@id="menu"]/li[2]/span').click()
        # 点击创建临时项目
        self.driver.find_element_by_xpath('//*[@id="addNew"]/div/div/div[1]/span').click()
        sleep(1)
        # 输入项目名称
        self.driver.find_element_by_xpath('//*[@id="aside-tabs"]/div[3]/div/div[2]/div[1]/ul/li[1]/input').send_keys(name)
        sleep(1)
        # 点击美腾科技有限公司
        self.driver.find_element_by_xpath('//*[@id="aside-tabs"]/div[3]/div/div[2]/div[2]/div[2]/div[1]/ul/div[1]/li/p').click()
        sleep(1)
        # 点击智冠信息事业部
        self.driver.find_element_by_xpath('//*[@id="aside-tabs"]/div[3]/div/div[2]/div[2]/div[2]/div[1]/ul/div[1]/li[2]/p').click()
        sleep(1)
        # 点击智能工厂研发部
        self.driver.find_element_by_xpath('//*[@id="aside-tabs"]/div[3]/div/div[2]/div[2]/div[2]/div[1]/ul/div[1]/li[1]/p').click()
        sleep(1)
        # 选中测试组
        self.driver.find_element_by_xpath('//*[@id="aside-tabs"]/div[3]/div/div[2]/div[2]/div[2]/div[1]/ul/div[1]/li[6]/label/span[1]/span').click()
        sleep(1)
        # 点击确定
        self.driver.find_element_by_xpath('//*[@id="aside-tabs"]/div[3]/div/div[2]/div[1]/div/button[1]').click()
        
                
if __name__ == "__main__":
 
    driver = webdriver.Chrome()
    LoginZhiXin(driver).login_zhixin("13820921009", "1111qqqq")
    sleep(1)
    LoginZhiYou(driver).login_zhiyou()
    sleep(1)
    CreateTemporaryProject(driver).create_temporary_project("测试临时项目1.1")     