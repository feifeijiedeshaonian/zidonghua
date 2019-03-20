from selenium import webdriver
from time import sleep
import sys
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\zhixin\login_zx')
from login__zhixin import LoginZhiXin
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\zhiyou\登录')
from login__zhiyou import LoginZhiYou
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\zhiyou_guanli\登录')
from login__zhiyou__guanli import LoginZhiYouGuanLi


class CreateCompanyProject():

    def __init__(self, driver):
        self.driver = driver

    def create_company_project(self, name):
        sleep(1)
        # 点击正式项目管理
        self.driver.find_element_by_xpath("//*[@id='leftBox']/ul/li[2]/ul/li/ul/li[1]").click()
        sleep(1)
        # 点击创建正式项目
        self.driver.find_element_by_xpath("//*[@id='pane-first']/div/div[1]/div/div[1]/button").click()
        sleep(1)
        # 点击创建新的正式项目
        self.driver.find_element_by_xpath(' //*[@id="pane-first"]/div/div[5]/div/div[2]/div/div[1]').click()
        sleep(1)
        # 公司项目命名
        self.driver.find_element_by_xpath('//*[@id="el_main"]/div/div[1]/div[1]/form/div[1]/div/div/input').send_keys(name)
        # 选择立项部门
        self.driver.find_element_by_xpath('//*[@id="el_main"]/div/div[1]/div[1]/form/div[2]/div/div/input').click()
        sleep(1)
        # 选择公司为立项部门
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/ul/div/li/label/span[1]/span').click()
        sleep(1)
        # 点击确定
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/span/button[2]/span').click()
        sleep(2)
        # 选择日期
        self.driver.find_element_by_xpath('//*[@id="el_main"]/div/div[1]/div[1]/form/div[3]/div/div').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[1]/table/tbody/tr[6]/td[5]/div/span').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[1]/table/tbody/tr[6]/td[5]/div/span').click()
        # 点击下一步
        self.driver.find_element_by_xpath('//*[@id="el_main"]/div/div[2]/button').click()
        # 点击下一步
        self.driver.find_element_by_xpath('//*[@id="el_main"]/div/div[2]/button[2]').click()
        # 点击下一步
        self.driver.find_element_by_xpath('//*[@id="el_main"]/div/div[2]/button[2]').click()
        sleep(1)
        # 选择承担部门
        self.driver.find_element_by_xpath('//*[@id="el_main"]/div/div[1]/div[4]/form/div[1]/div/div/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/ul/div/li/label/span[1]/span').click()
        # 点击确定
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/span/button[2]').click()
        sleep(1)
        # 添加人员
        self.driver.find_element_by_xpath('//*[@id="el_main"]/div/div[1]/div[4]/form/div[3]/div/button').click()        
        sleep(1)
        # 点击天津美腾科技有限公司
        self.driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[2]/div/ul/div[1]/li/p').click()
        sleep(1)
        # 选中综合服务部
        self.driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[2]/div/ul/div[1]/li[4]/label/span[1]/span').click()
        sleep(1)
        # 分担职务
        self.driver.find_element_by_xpath('//*[@id="tab-second"]').click()
        # 输入内容
        self.driver.find_element_by_xpath('//*[@id="pane-second"]/div/div/input').send_keys("测试")
        sleep(1)
        # 选择时间阶段
        self.driver.find_element_by_xpath('//*[@id="tab-third"]').click()
        # 选择长期
        self.driver.find_element_by_xpath('//*[@id="pane-third"]/div/p[2]/label/span[2]').click()
        # 点击确定
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/span/button[2]/span').click()
        # 项目参与人数
        self.driver.find_element_by_xpath('//*[@id="el_main"]/div/div[1]/div[4]/form/div[4]/div/div[1]/input').send_keys("6")       
        sleep(1)
        # 点击下一步
        self.driver.find_element_by_xpath('//*[@id="el_main"]/div/div[2]/button[2]').click()
        # 点击下一步
        self.driver.find_element_by_xpath('//*[@id="el_main"]/div/div[2]/button[2]').click()
        # 选择审批人
        self.driver.find_element_by_xpath('//*[@id="el_main"]/div/div[1]/div[6]/div[2]/div[1]/div/div/img').click()       
        sleep(1)
        # 点击天津美腾科技有限公司
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div/ul/div[1]/li/p').click()
        sleep(1)
        # 选择智冠信息事业部
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div/ul/div[1]/li[2]/p').click()
        # 选择智能工厂研发部
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div/ul/div[1]/li[1]/p').click()
        sleep(1)
        # 选择测试组
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div/ul/div[1]/li[6]/p').click()
        # 选择具体审批人
        sleep(1)
        for num in range(1, 14):
            name1 = driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div[2]/div/ul/div[2]/li[" + str(num) + "]/label/span[2]/span").text
            if name1 == '张凯1':
                driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div[2]/div/ul/div[2]/li[" + str(num) + "]/label/span[1]/span").click()
        sleep(1)
        # 点击确定
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/span/button[2]').click()
        # 选择抄送人
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="el_main"]/div/div[1]/div[6]/div[2]/div[2]/div/div/img').click()
        # 点击天津美腾科技有限公司
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div/ul/div[1]/li/p').click()
        sleep(1)
        # 选择智冠信息事业部
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div/ul/div[1]/li[2]/p').click()
        # 选择智能工厂研发部
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div/ul/div[1]/li[1]/p').click()
        sleep(1)
        # 选择测试组
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div/ul/div[1]/li[6]/label/span[1]/span').click()
        # 点击确定
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/span/button[2]').click()
        # 点击提交
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="el_main"]/div/div[2]/button[2]').click()
        sleep(1)

    def create1(self):
        # 点击正式项目管理
        self.driver.find_element_by_xpath('//*[@id="leftBox"]/ul/li[2]/ul/li/ul/li[1]').click()

     
if __name__ == "__main__":
    driver = webdriver.Chrome()
    CreateCompanyProject(driver).create1(3)