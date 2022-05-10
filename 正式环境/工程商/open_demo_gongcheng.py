from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.maximize_window()
url = 'http://mch.appykt.com/#/'
driver.get(url)
zhanghao = driver.find_element(By.XPATH,"//input[@type='text']")
zhanghao.send_keys('18354843')
pwd = driver.find_element(By.XPATH,'//input[@type="password"]')
pwd.send_keys('13202029682')

button = driver.find_element(By.XPATH,'//button[@type="button"]')
button.click()