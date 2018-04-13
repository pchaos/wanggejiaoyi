# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File    : untils.py

Description :

@Author :       pchaos

date：          18-4-10
-------------------------------------------------
Change Activity:
               18-4-10:
@Contact : p19992003#gmail.com                   
-------------------------------------------------
"""
__author__ = 'pchaos'

import sys
import os
import tempfile

def getTempdir():
    """
    获取临时目录
    :return:
    """
    return os.path.join(tempfile.gettempdir())

def getcurrentdir():
    return os.path.dirname(os.path.realpath(__file__))