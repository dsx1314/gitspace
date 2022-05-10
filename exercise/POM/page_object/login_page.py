from selenium.webdriver.common.by import By
from selenium import webdriver
from base_page import Basepage

class LoginPage(Basepage):
    # url
    url1 = "http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html"
    # 元素
    user = (By.NAME,"accounts")
    pwd = (By.NAME,"pwd")
    button = (By.XPATH,"/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button")

    def login(self,username,password):
        self.visit(self.url1)
        self.input(self.user,txt=username)
        self.input(self.pwd,txt=password)
        self.click(self.button)
        self.wait(3)


