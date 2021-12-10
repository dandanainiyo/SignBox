logo=r'''
     _______. __    _______ .__   __. .______     ______   ___   ___ 
    /       ||  |  /  _____||  \ |  | |   _  \   /  __  \  \  \ /  / 
   |   (----`|  | |  |  __  |   \|  | |  |_)  | |  |  |  |  \  V  /  
    \   \    |  | |  | |_ | |  . `  | |   _  <  |  |  |  |   >   <   
.----)   |   |  | |  |__| | |  |\   | |  |_)  | |  `--'  |  /  .  \  
|_______/    |__|  \______| |__| \__| |______/   \______/  /__/ \__\                                                                     
'''
##########################BILIBILI区设置##########################
bili=True#bilibili签到总开关
biliCookies=[{}]#哔哩哔哩账号cookie存放
paly=True#每日播放任务开关，True开启，False关闭
biliSign=True#每日签到任务开关，True开启，False关闭
coin=True#每日投币任务开关，True开启，False关闭
share=True#每日分享任务开关，True开启，False关闭

sleep=3#操作延时，请设置3秒以上延时以防出现问题！
multiply=1  #默认投币数
select_like=0 #投币时是否点赞，0：不点赞；1：点赞
progress=0#上报观看视频任务观看进度。单位为秒，默认为0
##########################原神区设置##########################
genshin=True#原神签到总开关
genshinCookies= []#哔哩哔哩账号cookie存放
##########################v2ex区设置##########################
v2ex=True#原神签到总开关
v2exCookies= []#哔哩哔哩账号cookie存放

##########################以下设置不要动##########################
bili_header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}
err=101
success=110