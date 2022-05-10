from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.common.by import By

# from test_demo.lib.yaml_load import load_yaml
# driver = self.driver
@pytest.fixture(scope='function',name='driver')
# @pytest.mark.parametrize('udata', load_yaml('../data/data_read.yaml'))
def open_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://ws.appykt.com/#/')
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/div[1]/div/form/div[1]/div/div/input').send_keys('83083541')
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/div[1]/div/form/div[2]/div/div/input').send_keys('13202029682')
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/div[1]/div/div[3]/button').click()
    yield driver
    sleep(3)
    # driver.quit()

# @pytest.mark.parametrize('udata', load_yaml('../data/data_read.yaml'))
def test_login(driver):
    # driver.find_element(By.XPATH,udata['login']).send_keys(udata['login2'])
    # driver.find_element(By.XPATH,udata['login3']).send_keys(udata['login4'])
    # driver.find_element(By.XPATH,udata['login5']).click()
        # 临停订单
# def test_ftzn(driver):
#     driver.execute_script("document.body.style.zoom='0.9';")
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[3]/div').click()
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[3]/ul/li[1]').click()
    sleep(3)
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[2]/div/div[1]/div/div/div/input').clear()
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[2]/div/div[1]/div/div/div/input').click()
    # 选择日期
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/span[1]/div/input').clear()
    driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div[1]/span[1]/div/input').send_keys('2022-01-01')
    # self.driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[2]/div/div[1]/div/div/div/input').send_keys('2022-02-01')
    # self.driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div[2]/button[2]').click()
    sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/button[2]/span').click()
    # self.driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[1]/div/div/input').send_keys('苏ACX333')
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[9]/div/button[1]').click()
    sleep(2)
    # self.driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[3]/div/div[4]/div/div/span[2]/div/div/input').click()
    # self.driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/li[5]').click()
    # self.driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[3]/div/div[4]/div/div/ul/li[2]').click()
    # 截图代码
    driver.get_screenshot_as_file("F:\\exercise\\picture\\a.png")
    # 月租订单
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[3]/ul/li[2]').click()
    # self.driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[1]/div/div/input').send_keys('粤XHM132')
    # 选择日期
    sleep(3)
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[2]/div/div[1]/div/div/div/input').clear()
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[2]/div/div[1]/div/div/div/input').click()
    sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[1]/span[1]/div/input').click()
    sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[1]/span[1]/div/input').clear()
    driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[1]/span[1]/div/input').click()
    driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[1]/span[1]/div/input').send_keys('2022-01-01')
    sleep(1)
    # self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/button[2]').click()
    # self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/button[2]/span').click()
    # self.driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[6]/div/button[1]/span').click()
    # self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/button[2]/span').click()
    # sleep(2)
    # self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/button[2]/span').click()
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[6]/div/button[1]/span').click()
    sleep(2)
    driver.get_screenshot_as_file("F:\\exercise\\picture\\b.png")
#       储值订单
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[3]/ul/li[3]').click()
    sleep(3)
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[2]/div/div[1]/div/div/div/input').clear()
    # self.driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[2]/div/div[1]/div/div/div/input').click()
    driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[1]/span[1]/div/input').click()

    # self.driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(7) > div.el-picker-panel__body-wrapper > div > div.el-date-picker__time-header > span:nth-child(1) > div > input').click()
    driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[1]/span[1]/div/input').clear()
    driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[1]/span[1]/div/input').click()
    driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div/div[1]/span[1]/div/input').send_keys('2022-01-08')
    sleep(1)
    # self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/button[2]').click()
    sleep(3)
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[6]/div/button[1]').click()

    sleep(1)
    driver.get_screenshot_as_file("F:\\exercise\\picture\\c.png")

    sleep(2)
    # 进出车辆
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[3]/ul/li[5]').click()
    # 选择日期
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/div/form/div[4]/div/div[1]/div/div/div/input').click()
    driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div/div[1]/span[1]/div/input').clear()
    driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[1]/span[1]/div/input').send_keys('2022-01-01')
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/div/form/div[5]/div/button[1]').click()
    #翻页
    sleep(2)
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[2]/div/div[4]/div/div/span[2]/div/div[1]/input').click()
    sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div[1]/ul/li[5]').click()
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/div/form/div[5]/div/button[1]').click()
    # self.driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/div/form/div[5]/div/button[1]').click()
    sleep(2)
    driver.get_screenshot_as_file("F:\\exercise\\picture\\d.png")
#         交易记录
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[4]/div').click()
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[4]/ul/li[1]').click()
    sleep(2)
    # self.driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/div/form/div[3]/div/div[1]/div/div/div/input').clear()
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/div/form/div[3]/div/div[1]/div/div/div/input').click()
    driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[1]/span[1]/div/input').click()
    driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[1]/span[1]/div/input').clear()
    driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[1]/span[1]/div/input').send_keys('2022-01-01')
    sleep(2)
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/div/form/div[4]/div/button[1]').click()
    sleep(1)
    driver.get_screenshot_as_file("F:\\exercise\\picture\\e.png")

    sleep(1)

#       交易记录
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[4]/ul/li[2]').click()
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/div/form/div[2]/div/div[1]/div/div/div/input').click()
    driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/div/div[1]/span[1]/div/input').click()
    driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/div/div[1]/span[1]/div/input').clear()
    driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/div/div[1]/span[1]/div/input').send_keys('2022-01-01')
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/div/form/div[3]/div/button[1]').click()

    sleep(1)
    driver.get_screenshot_as_file("F:\\exercise\\picture\\f.png")

    sleep(1)

#         月租车导入
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[7]/div').click()
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[7]/ul/li[2]').click()
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/div[2]/div/form/div/div/button[2]').click()

    # self.driver.find_element(By.XPATH,'/html/body/div[8]/div[2]/div/section/main/div/div/div/div/div[1]/div/div/em')
    driver.find_element(By.XPATH,'/html/body/div[8]/div[2]/div/section/main/div/div/div/div/div[1]/input').send_keys("F:\\exercise\\picture\\1.xls")

    sleep(0.5)
    driver.get_screenshot_as_file("F:\\exercise\\picture\\g.png")
    sleep(10)
    driver.get_screenshot_as_file("F:\\exercise\\picture\\g.png")
def test_shouye(driver):
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[1]/div').click()
    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/aside/div/div/div[2]/div/ul/li[1]/ul/li').click()
    sleep(1)
    # # driver.execute_script("document.body.style.zoom='0.8';")
    # sleep(1)
    # bottom = "window.scrollTo(0,document.body.scrollHeight)"
    # driver.execute_script(bottom)
    # sleep(1)
    # top = "var q=document.documentElement.scrollTop=0"
    # driver.execute_script(top)

    driver.find_element(By.XPATH,'//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/div[1]/form/div[2]/div/div/input[1]').click()
    driver.find_element(By.XPATH,"//div[@class='el-picker-panel__body-wrapper']/div[@class='el-picker-panel__body']/div/div/button[2]").click()
    driver.find_element(By.XPATH,"//div[@class='el-picker-panel__body-wrapper']/div[@class='el-picker-panel__body']/div[@class='el-picker-panel__content el-date-range-picker__content is-left']/table/tbody/tr[4]/td[4]").click()
    driver.find_element(By.XPATH,"//div[@class='el-picker-panel__body-wrapper']/div[@class='el-picker-panel__body']/div[@class='el-picker-panel__content el-date-range-picker__content is-left']/table/tbody/tr[4]/td[4]").click()
    sleep(0.5)
    driver.get_screenshot_as_file("F:\\exercise\\picture\\h.png")
if __name__ == '__main__':
    pytest.main(['-sv','-rerunfailures','test.py'])


