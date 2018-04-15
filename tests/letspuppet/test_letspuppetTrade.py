# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File    : test_letspuppetTrade.py

Description : 测试letspuppetTrade

@Author :       pchaos

date：          2018-4-10
-------------------------------------------------
Change Activity:
               18-4-10:
@Contact : p19992003#gmail.com                   
-------------------------------------------------
"""

from unittest import TestCase

import os
import json
from tools import tools
from letspuppet import *

__author__ = 'pchaos'


class TestletspuppetTrade(TestCase):

    def test_getsignaldb(self):
        theday = '20180404'
        filename = getsignaldbname(theday)
        if os.path.isfile(filename):
            print('filename: {}'.format(filename))
            self.assertTrue(filename is not None, "file not founded:{}".format(filename))
        else:
            self.fail('必须先要有{}测试文件'.format(filename))

        # 当前目录不存在，则返回系统临时目录+文件名
        theday = '20180410'
        filename = getsignaldbname(theday)
        print('filename: {}'.format(filename))
        self.assertTrue(not os.path.isfile(filename), "文件已存在：{}".format(filename))

    def test_getsignal(self):
        theday = '20180404'
        filename = getsignaldbname(theday)
        if os.path.isfile(filename):
            sig = getsignal(theday)
            print('signal: {}'.format(sig))
            self.assertTrue(sig is not None, "sig is None")
        else:
            self.fail('必须先要有{}测试文件'.format(filename))

        theday = '20180410'
        filename = getsignaldbname(theday)
        if not os.path.isfile(filename):
            # 从已有的文件复制到临时目录
            oday = '20180404'
            ofilename = getsignaldbname(oday)
            if os.path.isfile(ofilename):
                tools.cp(ofilename, filename)
            self.assertTrue(os.path.isfile(filename), "未复制成功文件：{}".format(filename))
        sig = getsignal(theday)
        print('signal: {}'.format(sig))
        self.assertTrue(sig is not None, "sig is None")

        # 删除临时文件
        if os.path.isfile(filename):
            tools.shell_exec("rm {}".format(filename))
            self.assertTrue(not os.path.isfile(filename), "未删除成功文件：{}".format(filename))

    def test_getsignaldf(self):
        theday = '20180404'
        filename = getsignaldbname(theday)
        if os.path.isfile(filename):
            signaldf = getsignal(theday)
            self.assertEqual(len(signaldf), 0, "测试数据为2018-04-04的数据，当前信号为0")
            # 返回包含一万天以前的信号
            signaldf = getsignal(theday,999999999)
            print('signal: {}'.format(signaldf))
            if signaldf.shape[0] > 0:
                print('signal index: {}'.format(signaldf.index)) # 此index和下面的index不同
                # signaldf = signaldf[signaldf['index'].isin(account[4])]
                signaldf = signaldf[signaldf['index'].isin(['mf'])]
                print('signal index: {}'.format(signaldf.index))
            self.assertTrue(signaldf is not None, "sig is None")
        else:
            self.fail('必须先要有{}测试文件'.format(filename))

    def test_account(self):
        accountfilename = 'accounts.json.example'
        with open(accountfilename) as f:
            accounts = json.load(f)
        for k,v in accounts.items():
            print("account name: {}".format(k))
            print("account : {}".format(v))