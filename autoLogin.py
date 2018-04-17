# -*- coding: utf-8 -*-
"""
-------------------------------------------------

@File    : autoLogin.py

Description : 自动登录华泰客户端

@Author :       pchaos

date：          18-4-16
-------------------------------------------------
Change Activity:
               18-4-16:
@Contact : p19992003#gmail.com                   
-------------------------------------------------
"""
__author__ = 'pchaos'
import  os
import autologin
from tools import *

def getclientname(clientname = 'ht_client'):
    return clientname

def getUserInfofromjson():
    filename= os.path.join(pwd(),'ht_client.json.env')
    if not os.path.isfile(filename):
        cp(filename+'.example', filename)
        assert 1==2, '先要配置文件:{}'.format(filename)

    upc=loadjson(filename)
    account, password, comm_password, exe_path =upc['user'],upc['password'], upc['comm_password'], upc['exe_path']
    return account, password, comm_password, exe_path

def getUserInfo():
    # 获取环境变量值
    defaultinfo = 'None'
    account = os.environ.get('HT_ACCOUNT') or defaultinfo
    password = os.environ.get('HT_password') or defaultinfo
    comm_password = os.environ.get('HT_comm_password') or defaultinfo
    if account == defaultinfo or password == defaultinfo or comm_password == defaultinfo:
        # 环境变量没有设置，则从文件中获取
        account, password, comm_password , exe_path= getUserInfofromjson()
    return account, password, comm_password, exe_path

def login(account, password, exe_path, comm_password):
    user = autologin.use(getclientname())
    user.prepare(
        user=account,
        password=password,
        exe_path = exe_path,
        comm_password=comm_password)

if __name__ == '__main__':
    account, password, comm_password, exe_path = getUserInfo()
    login(account, password, exe_path, comm_password)
