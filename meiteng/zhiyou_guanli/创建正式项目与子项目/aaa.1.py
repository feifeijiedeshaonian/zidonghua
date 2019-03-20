from HTMLTestRunner import HTMLTestRunner  
from email.mime.text import MIMEText  
from email.header import Header  
import smtplib  
import unittest  
import time  
import os  
  
#==============定义发送邮件==========  

def new_report(test_report):  
    lists = os.listdir(test_report)                                    #列出目录的下所有文件和文件夹保存到lists  
    lists.sort(key=lambda fn:os.path.getmtime(test_report + "\\" + fn))#按时间排序  
    file_new = os.path.join(test_report,lists[-1])                     #获取最新的文件保存到file_new  
    print(file_new)  
    return file_new  
  

def send_mail(file_new):  
    f = open(file_new,'rb')  
    mail_body = f.read()  
    f.close()  
  
    msg = MIMEText(mail_body,'html','utf-8')  
    msg['Subject'] = Header("自动化测试报告",'utf-8')  
  
    smtp = smtplib.SMTP()  
    smtp.connect('smtp.tjmeiteng.com')                                      #邮箱服务器  
    smtp.login("zhangkai@tjmeiteng.com","960811kai")                           #登录邮箱  
    smtp.sendmail("zhangkai@tjmeiteng.com<zhangkai@tjmeiteng.com>","wanghui01@tjmeiteng.com<wanghui01@tjmeiteng.com>",msg.as_string()) #发送者和接收者  
    smtp.quit()  
    print("邮件已发出！注意查收。")  
  
  
#======查找测试目录，找到最新生成的测试报告文件======  

if __name__ == "__main__":  
  
    test_dir = "C:\\Users\\LENOVO\\Desktop\\python\\美腾\\zhiyou_guanli\\创建正式项目与子项目"  
    test_report = "C:\\Users\\LENOVO\\Desktop\\张凯"  
  
    discover = unittest.defaultTestLoader.discover(test_dir,  
                                                   pattern = 'test_*.py')  
    now = time.strftime("%Y-%m-%d_%H-%M-%S")  
    filename = test_report + '\\' + now + 'result.html'  
    fp = open(filename,'wb')  
    runner = HTMLTestRunner(stream = fp,  
                            title = '测试报告',  
                            description = '用例执行情况：')  
    runner.run(discover)  
    fp.close()  
  
    new_report = new_report(test_report)  
    send_mail(new_report)     #发送测试报告  