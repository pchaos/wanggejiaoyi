# -*- coding: utf-8 -*-
"""
-------------------------------------------------

@File    : tradetools.py

Description :

@Author :

date：          18-4-15
-------------------------------------------------
Change Activity:
    2018 04 10  18：06：42 CST
    重构getsignal；首先再当前目录查找数据库，如果没有找到，则返回系统临时目录+数据库名

@Contact : p19992003#gmail.com                   
-------------------------------------------------
"""
import datetime
import os
import sqlite3
import time

import pandas as pd
import tushare as ts

from tools import tools, untils

__author__ = 'pchaos'


def gettoday():
    return datetime.datetime.now().strftime('%Y%m%d')


def getweekday():
    return datetime.datetime.now().date().weekday()


def strprice(p):
    return '%.3f' % p


def getsignal(today, lastsec= 90 ):
    """ 查询lastsec秒内的信号

    :param today: 查询日期
    :param lastsec: 查询lastsec内的数据； 默认为90秒内的信号有效
    :return:
    """
    dh = sqlite3.connect(getsignaldbname(today))
    last2min = time.time() - lastsec  # last 1.5 mins
    try:
        signaldf = pd.read_sql("SELECT * from signal where signal.time>%f" % last2min, dh)
        signaldf = signaldf.sort_values(['code', 'time'], ascending=[False, False])  # first trade then code then time??
        signaldf.index = signaldf['timestamp']
    except:
        signaldf = pd.DataFrame()
    dh.close()
    return signaldf


def getsignaldbname(today):
    """
    根据传入日期，返回信号数据库名
    首先再当前目录查找数据库，如果没有找到，则返回系统临时目录+数据库名

    :param today: 日期格式字符串；例如：‘’
    :return: 返回信号数据库名
    """
    filename = "trial_{0}.db".format(today)
    fullname = os.path.join(tools.pwd(), filename)
    if not os.path.isfile(fullname):
        fullname = os.path.join(untils.getTempdir(), filename)
    return fullname


def getlimit(code, aname):
    """

    :param code:
    :param aname:
    :return:
    """

    if code[:-1] == '15900' or code == '511880' or code == '511990' or code == '131810' or code == '204001':
        return 1000000
    else:
        if aname == 'a1':
            return 0  # 10000#0 means except money fund, no other trades are allowed
        elif aname == 'a2':
            return 10000


def getyesterdayc(c):
    """
    获取昨日收盘价
    :param c: 股票代码
    :return:
    """
    try:
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        df = ts.get_k_data(c, autype=None, index=False)
        df.index = df['date']
    except:
        return -1
    if df.index[-1] == today:
        return float(df.ix[-2, 'close'])
    else:
        return 0


def getallyesterdayc(clist):
    rt = {}
    for c in clist:
        p = getyesterdayc(c)
        if p not in [0, -1]:
            rt[c] = p
    return rt