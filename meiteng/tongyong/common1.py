from selenium import webdriver
from selenium. webdriver. support. wait import WebDriverWait
from selenium. webdriver. common. by import By


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