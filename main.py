from config import *
import biliSign,genshinSign
print(logo)
print('''
vesion:1.1
author:dandanya
''')
if genshin==True:
    print('------启动genshinSign------')
    genshinSign.task_run()
else:
    print('config.py中genshin变量未开启，genshinSign不启动')
if bili==True:
    print('------启动BiLiBiLiSign------')
    biliSign.task_run()
else:
    print('config.py中bili变量未开启，biliSign不启动')

