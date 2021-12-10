import requests,time,random,json
from config import *
from bs4 import BeautifulSoup
def v2exSign(cookie):
    url='https://www.v2ex.com/mission/daily'
    headers={
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi K30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.83 Mobile Safari/537.36',
        'cookie':cookie
    }
    r=requests.get(url=url,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser', from_encoding='utf-8')
    result=soup.find('span',class_='gray').text
    if result != '  每日登录奖励已领取':
        url = 'https://www.v2ex.com/mission/daily'
        r=requests.get(url=url,headers=headers)
        print(r.text)
    else:
        print('签到成功')

v2exSign(v2exCookies[0])