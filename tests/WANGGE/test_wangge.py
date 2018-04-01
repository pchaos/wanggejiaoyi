# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File    : test_wangge.py
Description :
@Author :       pchaos
date：          18-4-1
-------------------------------------------------
Change Activity:
               18-4-1:
@Contact : p19992003#gmail.com                   
-------------------------------------------------
"""
from unittest import TestCase
from WANGGE.wangge import *

__author__ = 'pchaos'


class TestWangge(TestCase):
    def setUp(self):
        self.high = 100.0
        self.low = 0.0
        self.n = 20  # 网格为20格
        # self.wg = wangGebase(self.high, self.low, self.n)
        self.wg = simpleWange(self.high, self.low, self.n)

    def tearDown(self):
        self.wg = None

    def test_doCaculate(self):
        wangge = self.wg()
        print(wangge)
        self.assertTrue(wangge[-1][1] == self.low, "caculate fault: {0} != {1}".format(wangge[-1][1], self.low))
        self.high = 1.323
        self.low = 0.414
        wangge = self.wg(self.high, self.low, self.n)
        print(wangge)
        self.assertTrue(wangge[-1][1] == self.low, "caculate fault: {0} != {1}".format(wangge[-1][1], self.low))
        self.n = 30
        wangge = self.wg(self.high, self.low, self.n)
        print(wangge)
        self.assertTrue(wangge[-1][1] == self.low, "caculate fault: {0} != {1}".format(wangge[-1][1], self.low))
        self.n = 40
        wangge = self.wg(self.high, self.low, self.n)
        print(wangge)
        self.assertTrue(wangge[-1][1] == self.low, "caculate fault: {0} != {1}".format(wangge[-1][1], self.low))
        self.assertTrue(wangge[0][1] == self.high, "caculate fault: {0} != {1}".format(wangge[0][1], self.high))
