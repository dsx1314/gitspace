import requests

url = 'http://yfweb.appykt.com/parking-uaa/oauth/token'
data = {"grant_type":"password","password":"e869ee21665414aae5bdc023dcfe7b91","scope":"all","username":"63010623"}
headers = {'Authorization':'Basic cGFyazpwYXJr','Content-Type':'application/x-www-form-urlencoded'}

res = requests.post(url=url,data=data,headers=headers)
response = res.json()

print(res.json())
token = response["data"]["accessToken"]

url = 'http://yfweb.appykt.com/parking-system/vistor/applyCode?mobileNumber=18302029682'
headers = {'Content-Type':'application/x-www-form-urlencoded',"Park-Mobile-Auth":f"{token}","X-Requser-With":"XMLHttpRequest"}
res = requests.get(url=url,headers=headers,)
print(res.json())