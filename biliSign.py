import requests,time,random,json
from config import *



def getRandomVideo(cookie):
        i=random.randint(1,101)
        url = 'http://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'
        res = requests.get(url=url, headers=bili_header,cookies=cookie)
        result=json.loads(res.text)
        if result['code']==0:
                videoList=result['data']["list"]
                choseVideo=videoList[i]
                print('当前选择了视频：%s up主：%s' %(choseVideo['title'],choseVideo['owner']['name']))
                return choseVideo['aid']
        else:
                return err

def userInfo(cookie):
        r=requests.get(url='http://api.bilibili.com/nav',headers=bili_header,cookies=cookie)
        user_info=json.loads(r.text)
        if user_info['code'] == 0:
                print('登录成功！')
                user_info=user_info['data']
                print('当前用户：%s 等级%d。'%(user_info['uname'],user_info['level_info']['current_level']))
                if user_info['level_info']['current_level'] < 6:
                        print('升级下一等级需达到的经验为:%d'%user_info['level_info']['next_exp'])
                return success
        else:
                print('登录失败，BiLiBiLiSign退出当前账号')
                return err


def getExp(cookie):
        url='http://api.bilibili.com/x/web-interface/coin/today/exp'
        r=requests.get(url=url,headers=bili_header,cookies=cookie)
        result=json.loads(r.text)
        if result['code'] == 0:
                return result['data']
        else:
                return err
def coinAdd(cookie,**kwargs):
        url='http://api.bilibili.com/x/web-interface/coin/add'
        if kwargs.get('aid') == None and kwargs.get('bid') == None :
                print('视频id未传入')
        else:
                if kwargs.get('bid') == None:
                        data={
                                'aid':kwargs['aid'],
                                'multiply':multiply,
                                'select_like':select_like,
                                'csrf':cookie['bili_jct']
                              }
                else:
                        data = {
                                'bvid': kwargs['bid'],
                                'multiply': multiply,
                                'select_like': select_like,
                                'csrf': cookie['bili_jct']
                        }
                r=requests.post(url=url,headers=bili_header,cookies=cookie,data=data)
                result=json.loads(r.text)
                code=result['code']
                if code == 0:
                        print('投币成功，数量为 %d'%multiply)
                        return success
                else:
                        print(result)
                        return err

def task_addCoin(cookie):
        print('投币任务开始...')
        err_flag=0
        while(True):
                if err_flag>=20:
                        print('错误次数过多，退出任务！')
                        break
                exp=getExp(cookie)
                if exp == err:
                        print('api请求失败')
                        err_flag += 1
                else:
                        print('当前已投币 %d '%(exp/10))
                        if exp<50:
                                aid=getRandomVideo(cookie)
                                if aid==err:
                                        print('获取视频失败')
                                        err_flag+=1
                                else:
                                        print('开始投币...')
                                        if coinAdd(cookie,aid=aid) == err:
                                                err_flag += 1
                                time.sleep(sleep)
                        else:
                                print('投币任务已完成...')
                                break
def shareVideo(cookie,**kwargs):
        url='https://api.bilibili.com/x/web-interface/share/add'
        if kwargs.get('aid') == None and kwargs.get('bid') == None :
                print('视频id未传入')
        else:
                if kwargs.get('bid') == None:
                        data={
                                'aid':kwargs['aid'],
                                'csrf':cookie['bili_jct']
                              }
                else:
                        data = {
                                'bvid': kwargs['bid'],
                                'csrf': cookie['bili_jct']
                        }
                r=requests.post(url=url,headers=bili_header,cookies=cookie,data=data)
                result=json.loads(r.text)
                code=result['code']
                if code == 0:
                        print('视频分享成功！')
                        return success
                else:
                        print('视频分享失败')
                        return err
def task_share(cookie):
        print('分享任务开始...')
        for i in range(20):
                if shareVideo(cookie,aid=getRandomVideo(cookie))==success:
                        print('分享任务已完成...')
                        return success
                else:
                        print('正在重试...')
        print('错误次数过多，退出任务！')
        return err
def task_sign(cookie):
        url='https://api.live.bilibili.com/sign/doSign'
        r = requests.get(url=url, headers=bili_header, cookies=cookie)
        result = json.loads(r.text)

        code = result['code']
        if code == 0:
                print('bilibili直播签到成功！')
                return success
        elif code == 1011040:
                print('重复签到')
                return success
        else:
                print('签到失败')
                return err
def getCid(cookie,**kwargs):
        url='http://api.bilibili.com/x/web-interface/view?'
        if kwargs.get('aid') == None and kwargs.get('bid') == None :
                print('视频id未传入')
        else:
                if kwargs.get('bid') == None:
                        url+='aid=%d'%kwargs['aid']
                else:
                        url+='bvid=%s'%kwargs['bid']
                r=requests.get(url=url,headers=bili_header,cookies=cookie)
                result=json.loads(r.text)
                code=result['code']
                if code == 0:
                        return result['data']['cid']
                else:
                        return err

def repotVideo(cookie,**kwargs):
        url='http://api.bilibili.com/x/click-interface/web/heartbeat'
        if kwargs.get('aid') == None and kwargs.get('bid') == None:
                print('视频id未传入')
        else:
                if kwargs.get('bid') == None:
                        cid=getCid(cookie,aid=kwargs['aid'])
                        if cid == err:
                                print('观看记录上报失败！')
                                return err
                        data = {
                                'aid': kwargs['aid'],
                                'progress':progress,
                                'cid':cid
                                }
                else:
                        cid = getCid(cookie, bid=kwargs['bid'])
                        if cid == err:
                                print('观看记录上报失败！')
                                return err
                        data = {
                                'bvid': kwargs['bid'],
                                'progress': progress,
                                'cid': cid
                        }
                r = requests.post(url=url, headers=bili_header, cookies=cookie, data=data)
                result = json.loads(r.text)
                code = result['code']
                if code == 0:
                        print('观看记录上报成功')
                        return success
                else:
                        print('观看记录上报失败!!')
                        return err
def task_palyVideo(cookie):
        print('开始播放视频任务...')
        for i in range(20):
                if repotVideo(cookie,aid=getRandomVideo(cookie))==success:
                        print('分享任务已完成...')
                        return success
                else:
                        print('正在重试...')
        print('错误次数过多，退出任务！')
        return err

def task_run():
        print('BiLiBiLiSign\n共检测到'+str(len(biliCookies))+'个账号')
        count=1
        for i in biliCookies:
                print('正在进行第'+str(count)+'个账号')
                if userInfo(i)==err:
                        continue
                if biliSign==True:
                        task_sign(i)
                        time.sleep(sleep)
                if paly==True:
                        task_palyVideo(i)
                        time.sleep(sleep)
                if coin==True:
                        task_addCoin(i)
                        time.sleep(sleep)
                if share==True:
                        task_share(i)
                        time.sleep(sleep)
                count+=1
        print('BiLiBiLi签到完成')






