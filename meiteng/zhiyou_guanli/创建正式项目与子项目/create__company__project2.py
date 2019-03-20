from selenium import webdriver
from time import sleep
from selenium. webdriver. common. by import By
import sys
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\zhixin\login_zx')
from login__zhixin1 import LoginZhiXin
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\zhiyou\登录')
from login__zhiyou2 import LoginZhiYou
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\zhiyou_guanli\登录')
from login__zhiyou__guanli1 import LoginZhiYouGuanLi
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\tongyong')
from common2 import Base


class CreateCompanyProject():

    def __init__(self, driver):
        self.driver = driver

    def create_company_project(self, name):
        sleep(1)
        # 点击正式项目管理
        Base.click(self, [By.XPATH, "//*[@id='leftBox']/ul/li[2]/ul/li/ul/li[1]"], self.driver)
        # 点击创建正式项目
        Base.click(self, [By.XPATH, "//*[@id='pane-first']/div/div[1]/div/div[1]/button"], self.driver)
        # 点击创建新的正式项目
        Base.click(self, [By.XPATH, '//*[@id="pane-first"]/div/div[5]/div/div[2]/div/div[1]'], self.driver)
        # 公司项目命名
        Base.sendKeys(self, [By.XPATH, '//*[@id="el_main"]/div/div[1]/div[1]/form/div[1]/div/div/input'], name, self.driver)
        Base.click(self, [By.XPATH, '//*[@id="el_main"]/div/div[1]/div[1]/form/div[1]/label'], self.driver)
        r2 = Base.is_alert(self)
        print(r2)
        # 选择立项部门
        Base.click(self, [By.XPATH, '//*[@id="el_main"]/div/div[1]/div[1]/form/div[2]/div/div/input'], self.driver)
        # 选择公司为立项部门
        Base.click(self, [By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/ul/div/li/label/span[1]/span'], self.driver)
        # 点击确定
        Base.click(self, [By.XPATH, '/html/body/div[2]/div/div[3]/span/button[2]/span'], self.driver)
        # 选择日期
        sleep(1)
        Base.click(self, [By.XPATH, '//*[@id="el_main"]/div/div[1]/div[1]/form/div[3]/div/div'], self.driver)
        sleep(1)
        Base.click(self, [By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[7]/td[1]/div/span'], self.driver)
        Base.click(self, [By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[7]/td[1]/div/span'], self.driver)
        # 点击下一步
        Base.click(self, [By.XPATH, '//*[@id="el_main"]/div/div[2]/button'], self.driver)
        # 点击下一步
        Base.click(self, [By.XPATH, '//*[@id="el_main"]/div/div[2]/button[2]'], self.driver)
        # 点击下一步
        Base.click(self, [By.XPATH, '//*[@id="el_main"]/div/div[2]/button[2]'], self.driver)
        # 选择承担部门
        Base.click(self, [By.XPATH, '//*[@id="el_main"]/div/div[1]/div[4]/form/div[1]/div/div/input'], self.driver)
        Base.click(self, [By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/ul/div/li/label/span[1]/span'], self.driver)
        # 点击确定
        Base.click(self, [By.XPATH, '/html/body/div[4]/div/div[3]/span/button[2]'], self.driver)
        # 添加人员
        sleep(1)
        Base.click(self, [By.XPATH, '//*[@id="el_main"]/div/div[1]/div[4]/form/div[3]/div/button'], self.driver)       
        # 点击天津美腾科技有限公司
        Base.click(self, [By.XPATH, '//*[@id="pane-first"]/div/div[2]/div/ul/div[1]/li/p'], self.driver)
        # 选中综合服务部
        Base.click(self, [By.XPATH, '//*[@id="pane-first"]/div/div[2]/div/ul/div[1]/li[4]/label/span[1]/span'], self.driver)
        # 分担职务
        Base.click(self, [By.XPATH, '//*[@id="tab-second"]'], self.driver)
        # 输入内容
        Base.sendKeys(self, [By.XPATH, '//*[@id="pane-second"]/div/div/input'], "测试", self.driver)
        # 选择时间阶段
        Base.click(self, [By.XPATH, '//*[@id="tab-third"]'], self.driver)
        # 选择长期
        Base.click(self, [By.XPATH, '//*[@id="pane-third"]/div/p[2]/label/span[2]'], self.driver)
        # 点击确定
        Base.click(self, [By.XPATH, '/html/body/div[5]/div/div[3]/span/button[2]/span'], self.driver)
        # 项目参与人数
        Base.sendKeys(self, [By.XPATH, '//*[@id="el_main"]/div/div[1]/div[4]/form/div[4]/div/div[1]/input'], "6", self.driver)      
        # 点击下一步
        sleep(1)
        Base.click(self, [By.XPATH, '//*[@id="el_main"]/div/div[2]/button[2]'], self.driver)
        # 点击下一步
        Base.click(self, [By.XPATH, '//*[@id="el_main"]/div/div[2]/button[2]'], self.driver)
        # 选择审批人
        sleep(1)
        Base.click(self, [By.XPATH, '//*[@id="el_main"]/div/div[1]/div[6]/div[2]/div[1]/div/div/img'], self.driver)     
        # 点击天津美腾科技有限公司
        Base.click(self, [By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div/ul/div[1]/li/p'], self.driver)
        # 选择智冠信息事业部
        Base.click(self, [By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div/ul/div[1]/li[2]/p'], self.driver)
        # 选择智能工厂研发部
        sleep(1)
        Base.click(self, [By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div/ul/div[1]/li[1]/p'], self.driver)
        # 选择测试组
        Base.click(self, [By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div/ul/div[1]/li[6]/p'], self.driver)
        # 选择具体审批人
        sleep(1)
        for num in range(1, 15):
            name1 = self.driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div[2]/div/ul/div[2]/li[" + str(num) + "]/label/span[2]/span").text
            if name1 == '张凯1':
                self.driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div[2]/div/ul/div[2]/li[" + str(num) + "]/label/span[2]/span").click()
                break
        # 点击确定
        Base.click(self, [By.XPATH, '/html/body/div[6]/div/div[3]/span/button[2]'], self.driver)
        # 选择抄送人
        sleep(1)
        Base.click(self, [By.XPATH, '//*[@id="el_main"]/div/div[1]/div[6]/div[2]/div[2]/div/div/img'], self.driver)
        # 点击天津美腾科技有限公司
        Base.click(self, [By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div/ul/div[1]/li/p'], self.driver)
        # 选择智冠信息事业部
        Base.click(self, [By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div/ul/div[1]/li[2]/p'], self.driver)
        # 选择智能工厂研发部
        sleep(1)
        Base.click(self, [By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div/ul/div[1]/li[1]/p'], self.driver)
        # 选择测试组
        Base.click(self, [By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div/ul/div[1]/li[6]/label/span[1]/span'], self.driver)
        # 点击确定
        Base.click(self, [By.XPATH, '/html/body/div[7]/div/div[3]/span/button[2]'], self.driver)
        # 点击提交
        sleep(1)
        Base.click(self, [By.XPATH, '//*[@id="el_main"]/div/div[2]/button[2]'], self.driver)


if __name__ == "__main__":

    driver = webdriver.Chrome()
    LoginZhiXin(driver).login_zhixin("13820921009", "1111qqqq")
    LoginZhiYou(driver).login_zhiyou()
    LoginZhiYouGuanLi(driver).login_zhiyou_guanli()
    CreateCompanyProject(driver).create_company_project("张凯测试公司项目1.9")       