from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://ws.appykt.com/#/')
driver.implicitly_wait(20)
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/div[1]/div/form/div[1]/div/div/input').send_keys('83083541')
driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/div[1]/div/form/div[2]/div/div/input').send_keys('13202029682')
driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/div[1]/div/div[3]/button').click()

# 车场管理-岗亭值守
driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[2]/div').click()
driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[2]/ul/li[7]').click()
driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/div/div/div/div/div/div/div').click()
sleep(3)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/button[2]/span').click()