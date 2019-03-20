import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
# import logging


def new_report(test_report):

    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report+'\\'+fn))
    file_new = os.path.join(test_report, lists[-1])
    return file_new


def send_email(file_new):

    username = 'zhangkai@tjmeiteng.com'
    password = '960811kai'
    sender = 'zhangkai@tjmeiteng.com'
    receiver = ['wanghui01@tjmeiteng.com']
    msg = MIMEMultipart('mixed')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['From'] = 'zhangkai@tjmeiteng.com<zhangkai@tjmeiteng.com>'
    msg['To'] = ";".join(receiver) 
    text = "自动化测试完成，结果请查看附件"
    text_plain = MIMEText(text, 'plain', 'utf-8')    
    msg.attach(text_plain)
    sendfile = open(file_new, 'rb').read()
    text_att = MIMEText(sendfile, 'base64', 'utf-8')
    text_att["Content-Type"] = 'application/octet-stream'
    text_att.add_header('Content-Disposition', 'attachment', filename='TestResult.html')
    msg.attach(text_att) 
    smtp = smtplib.SMTP()    
    smtp.connect('smtp.tjmeiteng.com')
    smtp.login(username, password)    
    smtp.sendmail(sender, receiver, msg.as_string())    
    smtp.quit()


# def get_windows_img(self):
#         self.logger = logging.getLogger(__name__)
#         file_path = 'E:\\screenshot'
#         rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
#         screen_name = file_path + rq + '.png'
#         print(screen_name)
#         try:
#             self.driver.get_screenshot_as_file(screen_name)
#             self.logger.info("Had take screenshot and save to folder : /screenshots")
#         except NameError as e:
#             self.logger.error("Failed to take screenshot! %s" % e)
#             self.get_windows_img()


if __name__ == "__main__":   
    test_dir = "C:\\Users\\LENOVO\\Desktop\\python\\美腾\\zhiyou_guanli\\创建正式项目与子项目"
    test_report = "E:\\html"
    discover = unittest.defaultTestLoader.discover(test_dir, 
                                                   pattern='test_*.py')
    now = time.strftime('%Y-%m-%d_%H_%M_%S_')
    filename = test_report+'\\' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'测试报告',
                            description=u'用例执行情况：')
    runner.run(discover)
    fp.close() 
    # 取最新测试报告
    new_report = new_report(test_report)
    # 发送邮件，发送最新测试报告html
    send_email(new_report)
