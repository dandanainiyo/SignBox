import requests,math,time,random,hashlib,json,string
from config import *
def getDs():
    md5 = hashlib.md5()
    s = '9nQiU3AV0rJSIBWgdynfoGMGKaklfbM7'
    t = str(int(time.time()))
    r = ''.join(random.sample(string.ascii_lowercase + string.digits, 6))
    c = MD5('salt=' + s + '&t=' + t + '&r=' + r)

    ds = t + ',' + r + ',' + c
    # print(ds)
    return ds
def MD5(text: str) -> str:
    md5 = hashlib.md5()
    md5.update(text.encode())
    return md5.hexdigest()

def getInfo(cookie):
    # cookie={
    #     'cookie_token':cookie_token,
    #     'account_id':account_id,
    #     'ltuid':account_id,
    #     '_MHYUUID':MHYUUID,
    #     'ltoken':ltoken,
    #     '_ga':ga,
    #     '_gid':gid
    # }
    print('开始获取登录信息...')
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'cookie': cookie
    }
    r=requests.get(url='https://api-takumi.mihoyo.com/binding/api/getUserGameRolesByCookie?game_biz=hk4e_cn',headers=headers)
    u=json.loads(r.text)
    userlist=u['data']['list'][0]
    if not userlist['game_uid']:
        print('信息获取失败，请检查cookie')
    else:
        print('信息获取成功')
        # print(userlist)
        return userlist


def GenShinSign(userlist,cookie):
    uid = userlist['game_uid']
    region = userlist['region']
    region_name = userlist['region_name']
    nickname = userlist['nickname']
    level = userlist['level']
    info='服务器：'+region_name+'\t当前账号：'+nickname+'\t等级：'+str(level)
    print(info)
    data = {
        'act_id':"e202009291139501",
        'region': region,
        'uid':uid
    }

    # print(data)
    header={
        'Accept': 'application/json, text/plain, */*',
        'DS': getDs(),
        'Origin': 'https://webstatic.mihoyo.com',
        'x-rpc-device_id': 'F8459954-D990-496-A49B-7BA82C0FE3CB',
        'x-rpc-app_version': '2.34.1',
        'x-rpc-client_type': '5',
        "x-rpc-device_id": "F8459954-D990-4961-A49B-7BA82C0FE3CB",
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) miHoYoBBS/2.3.0',
        'Referer':'https://webstatic.mihoyo.com/bbs/event/signin-ys/index.html?bbs_auth_required=true&act_id=e202009291139501&utm_source=bbs&utm_medium=mys&utm_campaign=icon',
        'Accept-Encoding': 'gzip, deflate, br',
        'cookie':cookie
    }
    print('开始签到...')
    req=requests.post(url='https://api-takumi.mihoyo.com/event/bbs_sign_reward/sign',headers=header,data=json.dumps(data, ensure_ascii=False))
    message = json.loads(req.text)
    if message['retcode']==0 and message["data"]["success"] == 0:
        print('签到成功！')
    elif message['retcode']==0 and message["data"]["success"] != 0:
        print('签到失败!账号风控,需要验证码')
    elif message['retcode']==-5003:
        print('签到失败!旅行者,你已经签到过了')
    else:
        print('签到失败!请检查设置')

def task_run():
        print('GenShinSign\n共检测到' + str(len(genshinCookies)) + '个账号')
        count = 1
        for i in genshinCookies:
            print('正在进行第' + str(count) + '个账号')
            userlist = getInfo(i)
            GenShinSign(userlist, i)
            count += 1
