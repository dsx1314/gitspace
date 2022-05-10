import time
from selenium import webdriver
from selenium.webdriver.common.by import By

WIDTH = 1600  # 宽度
HEIGHT = 700  # 高度
PIXEL_RATIO = 0.8  # 分辨率

mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.get('http://ws.appykt.com/#/')
driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/div[1]/div/form/div[1]/div/div/input').send_keys('83083541')
driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/div[1]/div/form/div[2]/div/div/input').send_keys('13202029682')
driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/div[1]/div/div[3]/button').click()

time.sleep(3)
# driver.close()