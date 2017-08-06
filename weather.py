#coding=utf-8
import urllib, json, os
from urllib import request

def weather(city):
    base_url = "https://free-api.heweather.com/v5/forecast?city="
    key = "&key=b59cc2987db5483a8b851ffe9c36ae42"
    url = base_url + city + key
    resp = urllib.request.urlopen(url)
    cont = resp.read().decode('utf-8') 
    s = json.loads(cont)
    s1 = s['HeWeather5']
    s2 = s1[0]
    s3 = s2['daily_forecast']
    return s3[0]['date'] + s3[0]['cond']['txt_d'] + '最高气温' + s3[0]['tmp']['max'] + '℃' + '最低气温' + s3[0]['tmp']['min'] + '℃' + '风力' + s3[0]['wind']['sc'] + s3[1]['date'] + s3[1]['cond']['txt_d'] + '最高气温' + s3[1]['tmp']['max'] + '℃' + '最低气温' + s3[1]['tmp']['min'] + '℃' + '风力' + s3[1]['wind']['sc'] + s3[2]['date'] + s3[2]['cond']['txt_d'] + '最高气温' + s3[2]['tmp']['max'] + '℃' + '最低气温' + s3[2]['tmp']['min'] + '℃' + '风力' +s3[2]['wind']['sc']

def get_token():
    url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=NyGe6y1tnRXQnX1KbcRPY672&client_secret=852a0c6d2213ab8d5e3a174d5fd92a48"
    resp = urllib.request.urlopen(url)
    cont = resp.read().decode('utf-8')
    s = json.loads(cont)
    return s['access_token']

#print (get_token())
print (weather('zhengzhou'))
url = "http://tsn.baidu.com/text2audio?tex=" + weather('zhengzhou')+ "&lan=zh&cuid=bc:30:7e:09:21:fd brd ff:ff:ff:ff:ff:ff&ctp=1&tok=" + get_token()
os.system('mpg123 "%s"'%(url))