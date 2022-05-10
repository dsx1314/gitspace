from selenium import webdriver
import unittest

from POM.page_object.login_page import LoginPage


class TestWeb(unittest.TestCase):
    def test_01(self):
        self.driver = webdriver.Chrome()
        LoginPage(self.driver).login(username="123456",password="123456")