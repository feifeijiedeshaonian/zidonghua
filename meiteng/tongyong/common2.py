from selenium import webdriver
from selenium. webdriver. support. wait import WebDriverWait
from selenium. webdriver. common. by import By
# from selenium.webdriver.support import expected_conditions as EC


class Base():

    def findElement(driver, locator):
        ele = WebDriverWait(driver, 10, 0.5). until(lambda x: x.find_element(*locator))
        return ele
        
    def sendKeys(self, locator, text, driver):
        ele = Base.findElement(self.driver, locator)
        ele.send_keys(text)

    def click(self, locator, driver):
        ele = Base.findElement(self.driver, locator)
        ele.click()

    def isElementExist(self, element):
        flag = True
        try:
            self.driver.find_element_by_xpath(element)
            return flag
        except:
            flag = False
            return flag

    # def is_alert(self):
    #     # 返回alert对象
    #     try:
    #         result = WebDriverWait(self.driver, 10, 0.5). until(EC.alert_is_present())
    #         return result
    #     except(RuntimeError):
    #         return False
 

if __name__ == "__main__":
    zentao = Base()
    loc1 = (By.ID, "account")
    loc2 = (By.NAME, "password")
    loc3 = (By.ID, "submit")
    driver = webdriver.Chrome()
    driver.get("https://www.zentao.net/user-login.html")
    zentao.sendKeys(loc1, "admin1", driver)
    zentao.sendKeys(loc2, "123456", driver)
    zentao.click(loc3, driver)