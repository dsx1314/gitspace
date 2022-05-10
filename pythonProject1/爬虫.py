import requests
import re

from yaml_deal import clear,read
from write_yaml import write_yaml_demo
import pytest

# @pytest.fixture(scope='session')
# def get_clear():
#     clear()




def test_login():
    url = 'https://fapi.appykt.com/parking-uaa/oauth/token'

    data = {"grant_type":"password","password":"e869ee21665414aae5bdc023dcfe7b91","scope":"all","username":"74046814"}
    headers = {'Authorization':'Basic cGFyazpwYXJr','Content-Type':'application/x-www-form-urlencoded'}



    res = requests.post(url=url,data=data,headers=headers)
    response = res.json()
    print(response)
    token = response["data"]["accessToken"]

    # write_yaml_demo({"token":response["data"]["accessToken"]})


    # print(token)
    print("-----------------------------------------------")

    url_02 = 'https://fapi.appykt.com/parking-order/parkingOrder/inAndOutOrderList'

    data_02 = {"current": "3",
    "size": "100",
    "status": "0",
    "parkId":"10010455",
    "keyword": "",
    "startDate": "1646816311",
    "endDate": "1649494711",
    "carType": "",
    "order": "desc",
    "prop": "intime"}

    headers_02 = {"Content-Type": "application/x-www-form-urlencoded","Park-Auth":token}

    res_demo = requests.post(url=url_02,headers=headers_02,data=data_02)
    result = res_demo.json()
    # print(res_demo.json())
    # result = res_demo.text

    # f = open('dsx2.csv', 'w')
    # f.write('carnumber\n')
    # for i in range(0,100):
    #     carnumber_demo = result["data"]["records"][i]["carnumber"]
    #     print(carnumber_demo)
    #     f.write(f'{carnumber_demo}\n')
    # f.close()

    content = res_demo.text
    # print(content)
    #
    # car = re.findall(r'"carnumber":"(.*?)",',content)
    #
    # car = [i[9:] for i in car if 'bbs' in i]
    #
    # print(car)