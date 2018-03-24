import json
import time
import requests

class Weather:

    def __init__(self, url):
        self.url = url
        self.headers={
            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0..9, image / webp, image / apng, * / *;q = 0.8',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Cache - Control': 'max - age = 0',
            'Connection': 'keep - alive',
            'Host': 'tj.nineton.cn',
            'Upgrade - Insecure - Requests': '1',
            'User - Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
        }

    def getResponse(self):
        res = json.loads(requests.get(self.url,headers=self.headers).text)
        return res

    def getData(self):
        data = self.getResponse()
        t = time.localtime(time.time())
        sj = "%s年%s月%s日%s点%s分"%(t[0],t[1],t[2],t[3],t[4])
        if data is not None:
            city = data['weather'][0]['city_name']
            text = data['weather'][0]['now']['text']
            temperature = data['weather'][0]['now']['temperature']
            pm25 = data['weather'][0]['now']['air_quality']['city']['pm25']
            quality = data['weather'][0]['now']['air_quality']['city']['quality']
            dressing = data['weather'][0]['today']['suggestion']['dressing']['details']
            sentence = '五幺二宿舍的兄弟们大家好,现在是北京时间'+sj+',今天'+city+'的天气情况如下：'+text+temperature+'度，空气质量'+quality+'，PM2.5指数为'+pm25+'，'+dressing+'谢谢使用'
            return sentence
        else:
            return '获取天气出错，请稍后重试'
