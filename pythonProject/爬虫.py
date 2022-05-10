from selenium import webdriver
from bs4 import BeautifulSoup

from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By

web = 'https://wk.baidu.com/view/4868ab29753231126edb6f1aff00bed5b9f37396?pcf=2&bfetype=new'
chromedriver_dir = 'D:\chromedriver_win32\chromedriver.exe'

options = webdriver.ChromeOptions()
# 伪装成iPhone
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3')

driver = webdriver.Chrome(chrome_options=options)
driver.get(web)

el_list = driver.find_elements(By.XPATH, '//*[@id="pageNo-1"]/div[1]/div/div/div/div[2]/div/p')
f = open('dsx.txt', 'w')
for el in el_list:
    print(el.text)
    f.write(f'{el.text}')
f.close()