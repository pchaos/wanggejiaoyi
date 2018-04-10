# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File    : normalizationd.py
Description : 归一化方法
@Author :       pchaos
date：          2018-4-10
-------------------------------------------------
Change Activity:
               2018-4-10:
@Contact : p19992003#gmail.com                   
-------------------------------------------------
"""
__author__ = 'pchaos'

def MaxMinNormalization(x,Max=None,Min=None):
    """
    (0,1)标准化;

    当Max或min为None时，Max、Min的取值为:
        Max=x.max()
        Min=x.min()
    :param x: numpy array
    :param Max: 默认：numpy.max()
    :param Min: 默认：numpy.min()
    :return: (0,1)标准化后的numpy array
    """
    if (Max is None or Min is None):
        Max=x.max()
        Min=x.min()
    x = (x - Min) / (Max - Min);
    return x;


def Z_ScoreNormalization(x,mu=None,sigma=None):
    """
    Z-score标准化;

    原始数据的均值（mean）和标准差（standard deviation）进行数据的标准化。
    经过处理的数据符合标准正态分布，即均值为0，标准差为1

    当mu或sigma为None时，mu、sigma的取值为:
        mu=x.mean()
        sigma=x.std()
    :param x: numpy array
    :param mu: 均值）用np.average()，
    :param sigma: 标准差）用np.std()
    :return: 标准正态分布
    """
    if (mu is None or sigma is None):
        mu=x.mean()
        sigma=x.std()
    x = (x - mu) / sigma;
    return x;