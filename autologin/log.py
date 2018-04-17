# -*- coding: utf-8 -*-
"""
-------------------------------------------------

@File    : log.py

Description :

@Author :       pchaos

date：          18-4-16
-------------------------------------------------
Change Activity:
               18-4-16:
@Contact : p19992003#gmail.com                   
-------------------------------------------------
"""
__author__ = 'pchaos'


import logging

log = logging.getLogger('easytrader')
log.setLevel(logging.DEBUG)
log.propagate = False

fmt = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s %(lineno)s: %(message)s')
ch = logging.StreamHandler()

ch.setFormatter(fmt)
log.handlers.append(ch)
