from selenium import webdriver
from time import sleep

class Basepage:

    STYLE = "background: pink; border: 2px solid red"
    # driver = webdriver.Chrome()
    # driver.implicitly_wait(10)
    # driver.maximize_window()
    def __init__(self,driver):
        self.driver = driver

    def visit(self,url1):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(url1)

    def locator(self,loc):
        return self.driver.find_element(*loc)

    # 点击元素背景为空
    def find(self,loc):
        element = self.locator(loc)
        self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",element,Basepage.STYLE)
        return element

    def input(self,loc,txt):
        self.find(loc).send_keys(txt)

    def click(self,loc):
        self.locator(loc).click()

    def wait(self,slep):
        sleep(slep)

    def quit(self):
        self.driver.quit()