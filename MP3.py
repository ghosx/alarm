import requests
import json
import os

class MP3:
    def __init__(self,apiKey,secretKey,content):
        self.apiKey = apiKey
        self.secretKey = secretKey
        self.content = content
        self.path = './1.mp3'

    def getToken(self):
        u = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"%(self.apiKey,self.secretKey)
        r = json.loads(requests.get(u).text)
        return r['access_token']

    def getMP3(self):
        token = self.getToken()
        url = "http://tsn.baidu.com/text2audio?lan=zh&ctp=1&cuid=ghosx&tok={}&tex={}&vol=9&per=0&spd=5&pit=5".format(token,self.content)
        mp3data = requests.get(url).content
        try:
            with open('./1.mp3','wb') as f:
                f.write(mp3data)
        except IOError:
            with open('./log.txt','w+') as log:
                log.write('写入mp3文件出错')
        else:
            return True

    def playmusic(self):
        os.system('cvlc ./1.mp3')