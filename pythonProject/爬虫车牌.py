from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException








url = 'http://mch.appykt.com/#/'

zhanghao = '//input[@type="text"]'

password = '//input[@type="password"]'

button = '//button[@type="button"]'

chechangguanli = '//span[contains(text(),"车场管理")]'

gangtingzhishou = '//span[contains(text(),"岗亭值守")]'

# choose_carchang = '//*[@id="my-master-app"]/div/header/div/div[1]/input'

# choose_click_two = '/html/body/div[2]/div[1]/div[1]/ul/li[2]'

click_three = '//*[@id="my-master-app"]/div/div/div/div/div/div/div/div'

button_two = '/html/body/div[3]/div/div[3]/button[2]'

rengongchuchang = '//*[@id="my-master-app"]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div/div/div/div[3]/div/button[1]'

fenye = '/html/body/div[2]/div[2]/div/section/main/div/div/div/div[2]/div/div/span[2]/div/div/span'

yibaiye = '//span[contains(text(),"100条/页")]'

qishisan = '//li[contains(text(),"73")]'

qishier = '//li[contains(text(),"72")]'

qishiyi = '//li[contains(text(),"71")]'

qishi = '//li[contains(text(),"70")]'

liushijiu = '//li[contains(text(),"69")]'

liushiba = '//li[contains(text(),"68")]'



driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(url)
driver.find_element(By.XPATH,zhanghao).send_keys('74046814')
driver.find_element(By.XPATH,password).send_keys('13202029682')
driver.find_element(By.XPATH,button).click()

driver.find_element(By.XPATH,chechangguanli).click()
driver.find_element(By.XPATH,gangtingzhishou).click()
# driver.find_element(By.XPATH,choose_carchang).click()
# driver.find_element(By.XPATH,choose_click_two).click()
driver.find_element(By.XPATH,click_three).click()
# driver.find_element(By.XPATH,button_two).click()
driver.find_element(By.XPATH,rengongchuchang).click()
sleep(2)
driver.find_element(By.XPATH,fenye).click()
driver.find_element(By.XPATH,yibaiye).click()
driver.find_element(By.XPATH,qishisan).click()
driver.find_element(By.XPATH,qishier).click()
driver.find_element(By.XPATH,qishiyi).click()
driver.find_element(By.XPATH,qishi).click()
driver.find_element(By.XPATH,liushijiu).click()
driver.find_element(By.XPATH,liushiba).click()
sleep(5)
try:
    el_list = driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div/section/main/div/div/div/div[1]/div[3]/table/tbody/tr')
    f = open('dsx3.txt', 'a+')
    for el in el_list:
        print(el.text)
        f.write(f'{el.text}')
    f.close()
except StaleElementReferenceException:
    print('---failed----')
