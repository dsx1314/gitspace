import requests


class TestApi:

    def test_car(self=None):


        # 车辆入场（上海非标）
        url = 'https://' \
              'parktest2.jtcx.sh.cn:80/' \
              'service/parking/data/parkplot/arrive/pd31011501206' \
              '?$appId=3201ac1e1599439b8e3522b31a4940ee&' \
              'nonce=1808310=&' \
              'curTime=1650676881&' \
              'checkSum=9adcde103774d5f7e9716608669439acebcf3cd1'
        # headers = {"sign":""}

        data = {
            "seq":"xxxxxx",
            "plateId":"粤A11111",
            "vehicleType":1,
            "laneType":1,
            "freeBerth":100,
            "parkType":1,
            # "datatime": "1650674778",
        }

        res = requests.post(url=url,json=data)
        print(res.text)