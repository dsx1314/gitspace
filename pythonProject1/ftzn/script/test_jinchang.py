import allure
import pytest
import requests

from ftzn.common.xlrd读取xls import read_xls
from ftzn.common.读出口的车辆 import read_out_xls
from 读取Excel import read_excel
from yaml_deal import clear,read

class TestApi:

    # test_cases = read_excel('../1.xlsx')
    test_cases = read_xls('F:\\pythonProject1\\ftzn\\data\\carnumber.xls')
    test_cases_out = read_out_xls('F:\\pythonProject1\\ftzn\\data\\out_car.xls')
    # @pytest.mark.parametrize(argnames='carnumber',argvalues=test_cases)
    # @allure.story('入场')
    # @allure.title('入场接口用例')
    # def test_in(self,carnumber):
    #
    #     url = 'https://fapi.appykt.com/parking-monitor/monitor/operatorcario'
    #
    #     headers = {"Content-Type": "application/x-www-form-urlencoded","Park-Auth":read()}
    #
    #     data = {"channelId": "422","parkId": "10006519","carnumber":carnumber }
    #
    #     res = requests.post(url=url, data=data, headers=headers)
    #
    #     print(res.json())

    @pytest.mark.parametrize(argnames='out_car',argvalues=test_cases_out)
    @allure.story('出场')
    @allure.title('出场接口用例')
    def test_out(self,out_car):

        url_01 = 'https://fapi.appykt.com/parking-monitor/monitor/operatorcario'

        headers_01 = {"Content-Type": "application/x-www-form-urlencoded","Park-Auth":read()}

        data_01 = {"channelId": "423","parkId": "10006519","carnumber":out_car,"triggerType":"4","serialNo":"1803000c5fdb"}

        res = requests.post(url=url_01, data=data_01, headers=headers_01)

        print(res.json())


        