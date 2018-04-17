# -*- coding: utf-8 -*-
"""
-------------------------------------------------

@File    : test_auotoLogin.py

Description :

@Author :       pchaos

date：          18-4-17
-------------------------------------------------
Change Activity:
               18-4-17:
@Contact : p19992003#gmail.com                   
-------------------------------------------------
"""
from unittest import TestCase
from autoLogin import *

__author__ = 'pchaos'


class TestAuotologin(TestCase):
    def test_getUserInfofromjson(self):
        account, password, comm_password, exe_path = getUserInfofromjson()
        self.assertIsNotNone(account, "account is None")
        self.assertIsNotNone(password, "password is None")
        self.assertIsNotNone(comm_password, "account is None")
        print(account, password, comm_password, exe_path)