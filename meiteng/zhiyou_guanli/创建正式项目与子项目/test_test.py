import unittest
from selenium import webdriver
import HTMLTestRunner
from create__company__project2 import CreateCompanyProject
from approval_company_project import ApprovalCompanyProject
import sys
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\zhixin\login_zx')
from login__zhixin1 import LoginZhiXin
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\zhiyou\登录')
from login__zhiyou2 import LoginZhiYou
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\zhiyou_guanli\登录')
from login__zhiyou__guanli1 import LoginZhiYouGuanLi
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\tongyong')
from common1 import Base


# # 继承TestCase这个类
class TestMethod(unittest.TestCase):
    '''hhhhhhhhh:jjj'''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def test1(self): 
        u'''qqq:4454545'''
        LoginZhiXin(self.driver).login_zhixin("13820921009", "1111qqqq")

    def test2(self): 
        LoginZhiYou(self.driver).login_zhiyou()
        
    # def test3(self):
    #     LoginZhiYouGuanLi(self.driver).login_zhiyou_guanli()

    # def test4(self):
    #     CreateCompanyProject(self.driver).create_company_project("张凯测试公司项目3.0")

    # def test5(self): 
    #     LoginZhiXin(self.driver).login_zhixin("15733189935", "1111qqqq")

    # def test6(self): 
    #     LoginZhiYou(self.driver).login_zhiyou()
        
    # def test7(self):
    #     LoginZhiYouGuanLi(self.driver).login_zhiyou_guanli()
 
    # def test8(self): 
    #     ApprovalCompanyProject(self.driver).approval_company_project("张凯测试公司项目3.0")

if __name__=="__main__":


     unittest.main()

    # filename = 'C:/Users/LENOVO/Desktop/zhangkai/testresult1.html'    #测试报告的存放路径及文件名
    # fp = open(filename, 'wb')    # 创测试报告html文件，此时还是个空文件

    # suite = unittest.TestSuite()   # 调用unittest的TestSuite(),理解为管理case的一个容器（测试套件）
    # suite.addTest(TestMethod('test1'))  # 向测试套件中添加用例，"TestMethod"是上面定义的类名，"test01"是用例名
    # suite.addTest(TestMethod('test2'))
    # suite.addTest(TestMethod('test3'))
    # suite.addTest(TestMethod('test4'))
    # suite.addTest(TestMethod('test5'))
    # suite.addTest(TestMethod('test6'))
    # suite.addTest(TestMethod('test7'))
    # suite.addTest(TestMethod('test8'))
    # runner = unittest.TextTestRunner()   # 执行套件中的用例
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='接口测试报告', description='测试结果如下: ')
    # #  stream = fp  引用文件流
    # #  title  测试报告标题
    # #  description  报告说明与描述
    # runner.run(suite)   # 执行测试
    # fp.close()   # 关闭文件流，将HTML内容写进测试报告文件
