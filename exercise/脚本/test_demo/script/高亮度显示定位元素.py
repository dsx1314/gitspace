from selenium import webdriver
from time import sleep

STYLE = "background: pink; border: 2px solid red;"

def find(driver,by,loc):
    element = driver.find_element(by,loc)
    driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",element,STYLE)
    return element

driver = webdriver.Chrome()
driver.get('http://ws.appykt.com/#/')
driver.implicitly_wait(10)
driver.maximize_window()
find(driver,'xpath','//*[@id="my-master-app"]/div/div[1]/div/form/div[1]/div/div/input').send_keys('83083541')
find(driver,'xpath','//*[@id="my-master-app"]/div/div[1]/div/form/div[2]/div/div/input').send_keys('13202029682')
find(driver,'xpath','//*[@id="my-master-app"]/div/div[1]/div/div[3]/button').click()

find(driver,'xpath','//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[3]/div').click()
find(driver,'xpath','//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[3]/ul/li[1]').click()
sleep(2)

find(driver,'xpath','//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[2]/div/div[1]/div/div/div/input').clear()
find(driver,'xpath','//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[2]/div/div[1]/div/div/div/input').click()

find(driver,'xpath','/html/body/div[2]/div[1]/div/div[1]/span[1]/div/input').clear()
find(driver,'xpath','/html/body/div[2]/div[1]/div/div[1]/span[1]/div/input').send_keys('2022-01-01')

sleep(2)
find(driver,'xpath','/html/body/div[2]/div[2]/button[2]/span').click()
find(driver,'xpath','//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[10]/div/button[1]').click()
sleep(2)
driver.get_screenshot_as_file("F:\\exercise\\脚本\\picture\\a.png")
sleep(5)

driver.quit()
print('----------------执行成功-----------------')