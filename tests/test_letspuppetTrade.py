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
from letspuppet import letspuppetTrade as lpt
import os
from tools import tools

__author__ = 'pchaos'


class TestletspuppetTrade(TestCase):

    def test_getsignaldb(self):
        theday = '20180404'
        filename = lpt.getsignaldb(theday)
        if os.path.isfile(filename):
            print('filename: {}'.format(filename))
            self.assertTrue(filename is not None, "file not founded:{}".format(filename))
        else:
            self.fail('必须先要有{}文件'.format(filename))

        # 当前目录不存在，则返回系统临时目录+文件名
        theday = '20180410'
        filename = lpt.getsignaldb(theday)
        print('filename: {}'.format(filename))
        self.assertTrue(not os.path.isfile(filename), "文件已存在：{}".format(filename))

    def test_getsignal(self):
        theday = '20180404'
        filename = lpt.getsignaldb(theday)
        if os.path.isfile(filename):
            sig = lpt.getsignal(theday)
            print('signal: {}'.format(sig))
            self.assertTrue(sig is not None, "sig is None")
        else:
            self.fail('必须先要有{}文件'.format(filename))

        theday = '20180410'
        filename = lpt.getsignaldb(theday)
        if not os.path.isfile(filename):
            # 从已有的文件复制到临时目录
            oday = '20180404'
            ofilename = lpt.getsignaldb(oday)
            if os.path.isfile(ofilename):
                tools.cp(ofilename, filename)
            self.assertTrue(os.path.isfile(filename), "未复制成功文件：{}".format(filename))
        sig = lpt.getsignal(theday)
        print('signal: {}'.format(sig))
        self.assertTrue(sig is not None, "sig is None")

        # 删除临时文件
        if os.path.isfile(filename):
            tools.shell_exec("rm {}".format(filename))
            self.assertTrue(not os.path.isfile(filename), "未删除成功文件：{}".format(filename))