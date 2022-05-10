import re
import time

import requests

class TestAPT:
    token = ""

    def test_login(self):
        url = 'https://fapi.appykt.com/parking-uaa/oauth/token'

        data = {"grant_type":"password","password":"e869ee21665414aae5bdc023dcfe7b91","scope":"all","username":"74046814"}
        headers = {'Authorization':'Basic cGFyazpwYXJr','Content-Type':'application/x-www-form-urlencoded'}



        res = requests.post(url=url,data=data,headers=headers)
        response = res.json()
        print(response)
        TestAPT.token = response["data"]["accessToken"]

        print("---------------------------------------------------")

    def test_02(self):
        url_02 = 'https://fapi.appykt.com/parking-system/vehicleOwner/importExcel'

        data_02 = {"file":"F:\\pythonProject1\\车辆导入模板.xls","parkId":"10010455"}

        headers_02 = {"Content-Type":"multipart/form-data","Park-Auth":TestAPT.token}

        result = requests.post(url=url_02,data=data_02,headers=headers_02)

        print(result.json())
        # content = result.text

        # car = re.findall(r'')




if __name__ == '__main__':
    TestAPT()
