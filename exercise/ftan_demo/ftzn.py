import re

import requests

# 登录
url = 'http://yfweb.appykt.com/parking-uaa/oauth/token'
data = {"grant_type":"password","password":"e869ee21665414aae5bdc023dcfe7b91","scope":"all","username":"83083541"}
headers = {'Authorization':'Basic cGFyazpwYXJr','Content-Type':'application/x-www-form-urlencoded'}

res = requests.post(url=url,data=data,headers=headers)
response = res.json()

print(res.json())
token = response["data"]["accessToken"]
# print(token)


url ='http://yfweb.appykt.com/parking-pay/orderManage/selectOrderList?current=1&size=20&prop=id&order=desc&orderType=0&startDate=1646064000&endDate=1648742399'
headers['Park-Auth'] =f'{token}'
res = requests.get(url=url,headers=headers)

print(res.json())

# 访客预约
url = 'http://yfweb.appykt.com/parking-system/visitor/page?current=1&size=20&prop=id&order=desc&parkId=10012423&reviewState=0'
headers['Park-Auth'] =f'{token}'

res = requests.get(url=url,headers=headers)

print(res.json())

# 岗亭值守
url = 'http://yfweb.appykt.com/parking-monitor/monitor/getWorkstation'
headers['Park-Auth'] =f'{token}'
headers = {"Content-Type": "application/x-www-form-urlencoded","Park-Auth":f"{token}"}
data ={"parkId":"10012423"}
res = requests.post(url=url,headers=headers,data=data)
response = res.text
print(response)
value = re.search('"businessId":"(.*?)","deviceSn"',response)
print(value)
# print(res.json())

# 进场
url = 'http://yfweb.appykt.com/parking-monitor/monitor/operatorcario'
data ={"channelId":"328","parkId":"10012423","carnumber":"粤ADFGH1"}
headers = {"Content-Type": "application/x-www-form-urlencoded","Park-Auth":f"{token}"}
res  = requests.post(url=url,data=data,headers=headers)

print(res.json())


url = 'http://yfweb.appykt.com/parking-system/invoiceRecord/rushRedFp'
data={"id":"439"}
headers = {"Content-Type": "application/x-www-form-urlencoded","Park-Auth":f"{token}"}
response = requests.post(url=url,data=data,headers=headers)
print(response.json())
res = response.text
with open('./data.txt','w',encoding='utf-8') as fp:
    fp.write(res)
    fp.write('\r\n')

print('success')