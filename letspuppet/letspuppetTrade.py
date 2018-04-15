# -*- coding: utf-8 -*-
"""
Author: 久久为功 ， chaos

Date: 2017-11-19
Support multil-thread for different accounts

Change Activity:
    2018 04 15  18：06：42 CST
    重构lphaTrade到单独的文件：alphaTrade.py；重命名alphaTrade为AlphaTrade
    将公用函数单独保存到tradetools.py

"""
from letspuppet import LogAll
import logging
import json

from letspuppet.alphatrade import AlphaTrade
from puppet.puppet_v4 import *

# 广发
# CTRADEEXETITLE = '广发证券核新网上交易系统7.62'
# 华泰
CTRADEEXETITLE = '网上股票交易系统5.0'


@LogAll.LogAll('Tp')
def main():
    time.sleep(2)  # wait for exe start up
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(funcName)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S')  # CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
    with open('accounts.json') as f:
        accounts = json.load(f)
    threadlist = []
    for k, v in accounts.items():
        threadlist.append(AlphaTrade(v, k))
        threadlist[-1].start()
    for t in threadlist:
        t.join()


if __name__ == '__main__':
    main()
