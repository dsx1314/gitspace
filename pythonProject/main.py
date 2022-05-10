from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.common.by import By


class TestPage:
    @pytest.fixture(scope='function',name='driver')
    def open_browser_login(driver):
        driver = webdriver.Chrome
        driver.get('http://ws.appykt.com/#/')
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, '//*[@id="my-master-app"]/div/div[1]/div/form/div[1]/div/div/input').send_keys('63010623')
        driver.find_element(By.XPATH, '//*[@id="my-master-app"]/div/div[1]/div/form/div[2]/div/div/input').send_keys('13202029682')
        driver.find_element(By.XPATH, '//*[@id="my-master-app"]/div/div[1]/div/div[3]/button').click()

        return driver

    def test_dingdan(self,driver):
        driver.find_element(By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[3]/div').click()
        driver.find_element(By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[3]/ul/li[1]').click()
        driver.find_element(By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/h4/div/div[1]/input').click()

if __name__ == '__main__':
    pytest.main(['-sv','main.py'])