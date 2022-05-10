
import random

import requests

# while True:
#     def get_pin():
#         number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#         letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K',
#                   'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#         total_set = number + letter
#
#         value_set = "".join(random.sample(total_set, 6))
#
#         return value_set
#
#     a=get_pin()
    # print(a)

    # 登录
#     测试环境
url = 'http://yfweb.appykt.com/parking-uaa/oauth/token'

# 正式环境
# url_mch = 'https://fapi.appykt.com/parking-uaa/oauth/token'

data = {"grant_type":"password","password":"e869ee21665414aae5bdc023dcfe7b91","scope":"all","username":"54771134"}
headers = {'Authorization':'Basic cGFyazpwYXJr','Content-Type':'application/x-www-form-urlencoded'}

res = requests.post(url=url,data=data,headers=headers)
response = res.json()

print(res.json())
token = response["data"]["accessToken"]
print(f'{token}\n')
while True:
    def get_pin(self):
        number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K',
                      'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        total_set = number + letter
        u_len = random.randint(5,5)
        value_set = "".join([random.choice(total_set) for i in range(u_len)])

        return value_set

    def dsx(self):
        Chinese = ['粤', '京', '鲁', '贵', '云']
        hanzi = "".join(random.sample(Chinese,1))
        return hanzi
    def english(self):
        letter1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K',
                  'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        yingyu = "".join(random.sample(letter1, 1))
        return yingyu

    c = english(self=None)
    # print(c)

    b = dsx(self=None)
    # print(b)

    a = get_pin(self=None)

    # dsx01 = f'{b}{c}{a}'
    # print(dsx01)
    # with open('./data.txt', 'w', encoding='utf-8') as fp:
    #     fp.write(dsx01)
    #     fp.write('\r\n')


    # 进场
    url = 'http://yfweb.appykt.com/parking-monitor/monitor/operatorcario'
    # url2 = 'https://fapi.appykt.com/parking-monitor/monitor/operatorcario'
    data ={"channelId":"404","parkId":"10016605","carnumber":f"{b}{c}{a}"}
    headers = {"Content-Type": "application/x-www-form-urlencoded","Park-Auth":f"{token}"}
    res  = requests.post(url=url,data=data,headers=headers)
    print(res.json())


    # url01 = 'http://yfweb.appykt.com/parking-monitor/monitor/operatorcario'
    # # url2 = 'https://fapi.appykt.com/parking-monitor/monitor/operatorcario'
    # data ={"channelId":"405","parkId":"10016605","carnumber":f"{b}{c}{a}"}
    # headers = {"Content-Type": "application/x-www-form-urlencoded","Park-Auth":f"{token}"}
    # res  = requests.post(url=url01,data=data,headers=headers)
    # print(res.json())
    # 出场
    # url1 = 'http://yfweb.appykt.com/parking-monitor/monitor/operatorcario'
    # data ={"parkId":"10014883","carnumber":f"{b}{a}","recognizeId":"1646383638521fjedinf","serialNo":"1803000c5fdb",
    #        "triggerType":"4","channelId":"329"}
    #
    # res = requests.post(url=url1,data=data,headers=headers)
    #
    # print(res.json())