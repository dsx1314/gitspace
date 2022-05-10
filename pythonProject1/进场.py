import re

import pytest
import requests
from 读取Excel import read_excel
from yaml_deal import clear, read


class TestApi:
    test_cases = read_excel('F:\\pythonProject1\\1.xlsx')

    @pytest.mark.parametrize(argnames='carnumber', argvalues=test_cases)
    def test_in(self, carnumber):
        url = 'https://fapi.appykt.com/parking-monitor/monitor/operatorcario'

        headers = {"Content-Type": "application/x-www-form-urlencoded", "Park-Auth": read()}

        data = {"channelId": "388", "parkId": "10010455", "carnumber": carnumber}

        res = requests.post(url=url, data=data, headers=headers)

        result = res.json()

        # 正则表达式提取
        time = re.search("'time':(.*?)}",str(result))
        print(time.group())


        # print(res.json())

