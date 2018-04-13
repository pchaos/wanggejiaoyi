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

__author__ = 'pchaos'


class TestletspuppetTrade(TestCase):

    def test_getsignal(self):
        theday='20180404'
        sig=lpt.getsignal(theday)
        print(sig)
        self.fail()

