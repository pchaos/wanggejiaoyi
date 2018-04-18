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
import os
import autologin
from tools import *

CCLIENTNAME = 'ht_client'
CFILENAME = 'ht_client.json.env'


def getclientname(clientname=CCLIENTNAME):
    return clientname


def getUserInfofromjson(jsonFilename=CFILENAME):
    filename = os.path.join(pwd(), jsonFilename)
    if not os.path.isfile(filename):
        if os.path.isfile(filename + '.example'):
            cp(filename + '.example', filename)
        assert 1 == 2, '先要配置文件:{}'.format(filename)

    upc = loadjson(filename)
    account, password, comm_password, exe_path = upc['user'], upc['password'], upc['comm_password'], upc['exe_path']
    return account, password, comm_password, exe_path


def getUserInfo(jsonFilename=None):
    if jsonFilename is None:
        # 获取环境变量值
        defaultinfo = 'None'
        account = os.environ.get('HT_ACCOUNT') or defaultinfo
        password = os.environ.get('HT_password') or defaultinfo
        comm_password = os.environ.get('HT_comm_password') or defaultinfo
        if account == defaultinfo or password == defaultinfo or comm_password == defaultinfo:
            # 环境变量没有设置，则从文件中获取
            account, password, comm_password, exe_path = getUserInfofromjson()
    else:
        account, password, comm_password, exe_path = getUserInfofromjson(jsonFilename)
    return account, password, comm_password, exe_path


def login(account, password, exe_path, comm_password):
    user = autologin.use(getclientname())
    user.prepare(
        user=account,
        password=password,
        exe_path=exe_path,
        comm_password=comm_password)


if __name__ == '__main__':
    import optparse
    # 命令行参数 filename,通过配置文件改变登录参数
    parser = optparse.OptionParser()

    parser.add_option('-f', '--fileName',
                      action="store", dest="filename",
                      help="file name", default=CFILENAME)

    options, args = parser.parse_args()

    print('Query string:', options.filename)
    jsonfile = options.filename
    account, password, comm_password, exe_path = getUserInfo(jsonfile)
    login(account, password, exe_path, comm_password)
