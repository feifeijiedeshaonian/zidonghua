from selenium import webdriver
from time import sleep
# 复制
# import keys模块
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\tongyong')
from common2 import Base
sys.path.append(r'C:\Users\LENOVO\Desktop\python\美腾\zhixin\login_zx')
from login__zhixin1 import LoginZhiXin


driver = webdriver.Chrome()
LoginZhiXin(driver).login_zhixin("13820921009", "1111qqqq")
sleep(1)
# 搜索张超
driver.find_element_by_id("search-input").send_keys("张超")
sleep(1)
driver.get_screenshot_as_file("E:\\screenshot\\sousuozhangchao.png")
sleep(1)
driver.find_element_by_xpath("//*[@id='app']/div/section/header/div[1]/ul/li[1]").click()
# 发送文字
driver.find_element_by_class_name("editor").send_keys("安吉拉发士大夫立刻涉及到法律撒旦解放了撒娇离开对方沙发看到啥开朗大方奥卡福哈斯的山东分局撒和快乐和反抗拉萨符合贷款四点艾灸疗法还是老地方傻大姐")
driver.get_screenshot_as_file("E:\\screenshot\\发送文字1.png")
driver.find_element_by_xpath('//*[@id="app"]/div/section/section/div[2]/div/div[2]/div/div[2]/div[2]/div/button').click()
#   鼠标右击
# ActionChains(driver)：调用ActionChains()类，并将浏览器驱动browser作为参数传入
# context_click(right_click)：模拟鼠标双击，需要传入指定元素定位作为参数
# perform()：执行ActionChains()中储存的所有操作，可以看做是执行之前一系列的操作
# 定位到要右击的元素
sleep(1)
right_click = driver.find_element_by_xpath('//*[@id="scroll-body"]/li/div/div[2]/div/p')
# 对定位到的元素执行右击操作
try:
    ActionChains(driver).context_click(right_click).perform()
    print('成功右击')
except Exception as e:
    print('fail', e.value)
# 撤回
driver.find_element_by_xpath('//*[@id="message-container"]/ul[2]/li[1]/button').click()
sleep(1)
driver.get_screenshot_as_file("E:\\screenshot\\撤回.png")
# 发送文字
driver.find_element_by_class_name("editor").send_keys("安吉拉发士大夫立刻涉及到法律撒旦解放了撒娇离开对方沙发看到啥开朗大方奥卡福哈斯的山东分局撒和快乐和反抗拉萨符合贷款四点艾灸疗法还是老地方傻大姐")
driver.get_screenshot_as_file("E:\\screenshot\\发送文字2.png")
driver.find_element_by_xpath('//*[@id="app"]/div/section/section/div[2]/div/div[2]/div/div[2]/div[2]/div/button').click()
#   鼠标右击
sleep(1)
right_click = driver.find_element_by_xpath('//*[@id="scroll-body"]/li/div/div[2]/div/p')
try:
    ActionChains(driver).context_click(right_click).perform()
    print('成功右击')
except Exception as e:
    print('fail', e.value)
# 删除
driver.find_element_by_xpath('//*[@id="message-container"]/ul[2]/li[2]/button').click()
sleep(1)
driver.get_screenshot_as_file("E:\\screenshot\\删除.png")
# 发送文字
driver.find_element_by_class_name("editor").send_keys("安吉拉发士大夫立刻涉及到法律撒旦解放了撒娇离开对方沙发看到啥开朗大方奥卡福哈斯的山东分局撒和快乐和反抗拉萨符合贷款四点艾灸疗法还是老地方傻大姐")
driver.get_screenshot_as_file("E:\\screenshot\\发送文字2.png")
driver.find_element_by_xpath('//*[@id="app"]/div/section/section/div[2]/div/div[2]/div/div[2]/div[2]/div/button').click()
# 鼠标右击
sleep(1)
click1 = driver.find_element_by_xpath('//*[@id="scroll-body"]/li[2]/div/div[2]/div/p')
try:
    ActionChains(driver).context_click(click1).perform()
    print('成功右击')
except Exception as e:
    print('fail', e.value)
# 复制
driver.find_element_by_xpath('//*[@id="message-container"]/ul[2]/li[3]/button').click()
sleep(1)
# 模拟鼠标复制（ctrl+c）
driver.find_element_by_class_name('editor').send_keys(Keys.CONTROL,'v')
sleep(1)
driver.get_screenshot_as_file("E:\\screenshot\\复制.png")
# 将复制内容发送出去
driver.find_element_by_xpath('//*[@id="app"]/div/section/section/div[2]/div/div[2]/div/div[2]/div[2]/div/button').click()
# 鼠标右击
click1 = driver.find_element_by_xpath('//*[@id="scroll-body"]/li[2]/div/div[2]/div/p')
try:
    ActionChains(driver).context_click(click1).perform()
    print('成功右击')
except Exception as e:
    print('fail', e.value)
# 转发
driver.find_element_by_xpath('//*[@id="message-container"]/ul[2]/li[4]/button').click()
# 选择收件人
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/section/div[1]/div/div/input').send_keys("任少龙")
sleep(1)
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/section/div[1]/ul/li[1]').click()
# 点击确定
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[3]/div/button').click()
# 切换到任少龙界面
sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/section/section/div[1]/div/ul[1]/li[1]/div[2]/div[1]/p[1]').click()
driver.get_screenshot_as_file("E:\\screenshot\\转发.png")