from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.common.by import By



@pytest.fixture(scope='function',name='driver')
def open_browser_login():
    driver = webdriver.Chrome()
    url = 'http://ws.appykt.com/#/'
    driver.get(url=url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.find_element(By.XPATH, '//*[@id="my-master-app"]/div/div[1]/div/form/div[1]/div/div/input').send_keys('63010623')
    driver.find_element(By.XPATH, '//*[@id="my-master-app"]/div/div[1]/div/form/div[2]/div/div/input').send_keys('13202029682')
    driver.find_element(By.XPATH, '//*[@id="my-master-app"]/div/div[1]/div/div[3]/button').click()

    return driver
    sleep(2)

def test_dingdan(driver):
    driver.find_element(By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[3]/div').click()
    driver.find_element(By.XPATH, '//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[3]/ul/li[1]').click()
    driver.find_element(By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/h4/div/div[1]/input').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[2]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[9]/div/button[3]/span').click()
    sleep(2)
    driver.get_screenshot_as_file('F:\\pythonProject\\1.png')

# 组合查询  粤OP9876
    driver.find_element(By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[1]/div/div/input').send_keys('粤OP9876')
    driver.find_element()
if __name__ == '__main__':
    pytest.main(['-sv','test_dingdan.py'])