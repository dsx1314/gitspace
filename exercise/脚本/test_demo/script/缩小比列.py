from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()
sleep(1)
url = 'http://ws.appykt.com/#/'
driver.get(url=url)
sleep(3)
driver.execute_script("document.body.style.zoom='0.9';")