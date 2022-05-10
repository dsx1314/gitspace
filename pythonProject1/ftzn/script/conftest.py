import requests
import re
from time import sleep
from ftzn.common.修改Excel的数据 import remove_demo
from ftzn.common.写车牌号码 import get_car_number
from ftzn.common.读取txt import read_txt
from yaml_deal import clear,read
from write_yaml import write_yaml_demo
import pytest


# 控制台中文
from typing import List
import sys
sys.dont_write_bytecode = True

# def pytest_collection(session:"Session",config:"Config",items:List["Item"]) ->None:
#     for item in items:
#         item.name = item.name.encode("utf-8").decode("unicode-escape")
#         item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")




@pytest.fixture(scope='session',autouse=True)
def login():
    clear()
    sleep(1)
    get_car_number()
    sleep(1)
    read_txt()
    sleep(1)
    remove_demo()
    sleep(1)
    url = 'https://fapi.appykt.com/parking-uaa/oauth/token'
    data = {"grant_type":"password","password":"e869ee21665414aae5bdc023dcfe7b91","scope":"all","username":"74046814"}
    headers = {'Authorization':'Basic cGFyazpwYXJr','Content-Type':'application/x-www-form-urlencoded'}
    res = requests.post(url=url,data=data,headers=headers)
    response = res.json()
    print(response)
    token = response["data"]["accessToken"]

    write_yaml_demo({"token":response["data"]["accessToken"]})

    yield
    # print(token)
    print("-----------------------------------------------")

    # url_02 = 'https://fapi.appykt.com/parking-order/parkingOrder/inAndOutOrderList'
    #
    # data_02 = {"current": "3",
    # "size": "100",
    # "status": "0",
    # "parkId":"10010455",
    # "keyword": "",
    # "startDate": "1646816311",
    # "endDate": "1649494711",
    # "carType": "",
    # "order": "desc",
    # "prop": "intime"}
    #
    # headers_02 = {"Content-Type": "application/x-www-form-urlencoded","Park-Auth":read()}
    #
    # res_demo = requests.post(url=url_02,headers=headers_02,data=data_02)
    # result = res_demo.json()
    # print(res_demo.json())
    #
    # f = open('dsx2.csv', 'w')
    # f.write('carnumber\n')
    # for i in range(0,100):
    #     carnumber_demo = result["data"]["records"][i]["carnumber"]
    #     print(carnumber_demo)
    #     f.write(f'[{i}:{carnumber_demo}]\n')
    # f.close()