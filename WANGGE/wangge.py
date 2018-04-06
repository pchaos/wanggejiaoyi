# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name：     wangge.py
Description :
Author :       pchaos
date：          2018-04-01
-------------------------------------------------
Change Activity:
               ${DATE}:
@Contact : p19992003#gmail.com
-------------------------------------------------
"""
__author__ = 'pchaos'

import numpy as np


class wangGebase():
    """
    网格基础类
    返回举例：
    序号	当时价格	网格	仓位%	估值动率
    0	￥1.323	0.04545	0.00%	52.33%
    1	￥1.278	0.04545	5.00%	47.10%
    2	￥1.232	0.04545	10.00%	41.86%
    3	￥1.187	0.04545	15.00%	36.63%
    4	￥1.141	0.04545	20.00%	31.40%
    5	￥1.096	0.04545	25.00%	26.17%
    6	￥1.050	0.04545	30.00%	20.93%
    7	￥1.005	0.04545	35.00%	15.70%
    8	￥0.959	0.04545	40.00%	10.47%
    9	￥0.914	0.04545	45.00%	5.23%
    10	￥0.869	0	50.00%	0.00%
    11	￥0.823	0.04545	55.00%	-5.23%
    12	￥0.778	0.04545	60.00%	-10.47%
    13	￥0.732	0.04545	65.00%	-15.70%
    14	￥0.687	0.04545	70.00%	-20.93%
    15	￥0.641	0.04545	75.00%	-26.17%
    16	￥0.596	0.04545	80.00%	-31.40%
    17	￥0.550	0.04545	85.00%	-36.63%
    18	￥0.505	0.04545	90.00%	-41.86%
    19	￥0.459	0.04545	95.00%	-47.10%
    20	￥0.414	0.04545	100.00%	-52.33%

    """

    # 保存网格
    _wangge = None  # 计算后的网格

    def __init__(self, wghigh, wglow, fgN=20):
        """
        初始化网格
        :param wghigh: 网格顶部价格
        :param wglow: 网格底部价格
        :param fgN: 网格拆分份数 默认为20间隔
        """
        self._setvaues(wghigh, wglow, fgN)

    def _setvaues(self, wghigh, wglow, fgN):
        checked = self.__checkValue(wghigh, fgN)
        assert checked, "网格顶部价格或者分隔份数不能为0！"
        self._high = wghigh
        self._low = wglow
        self._n = fgN + 1

    def __checkValue(self, wghigh, fgN, wglow=0):
        """
        判断网格顶部价格或者分隔份数是否有效，有效返回True
        :param wghigh:
        :param fgN:
        :param wglow:
        :return:
        """
        return wghigh * fgN > 0

    def __call__(self, wghigh=0, wglow=0, fgN=0):
        if (wghigh != self._high or wglow != self._low or fgN != self._n or self._wangge is None or self.__checkValue(
                wghigh, fgN)):
            # 计算网格
            if self.__checkValue(wghigh, fgN):
                self._setvaues(wghigh, wglow, fgN)
            self.__caculateWangge()
        return self._wangge

    def __caculateWangge(self):
        self.doCaculate()

    def doCaculate(self):
        """
        虚函数，计算网格的过程在此写，默认为均分间隔。
        需要改变间隔的，子类中重写间隔逻辑
        :return: 无
        """
        # 列数量
        j = 5
        dt = np.dtype([('序号', np.int8), ('当时价格', np.float), ('网格间距', np.float), ('仓位%', np.float),
                       ('估值动率%', np.float)])
        self._wangge = np.zeros((self._n), dtype=dt)
        # 网格间距
        jianju = (self._high - self._low) / (self._n - 1)
        #  居中价格
        jz = np.round((self._high + self._low) / 2, 4)
        print("居中价格：{0}, 网格顶价格：{1}, 网格底部价格：{2}, 网格数量：{3}".format(jz, self._high, self._low, self._n - 1))
        for i in range(0, self._n):
            # 按顺序为： 序号	当时价格	网格	仓位%	估值动率%
            self._wangge[i][0] = i
            self._wangge[i][1] = np.round(jz + jianju * ((self._n - 1) / 2 - i), 4)
            self._wangge[i][2] = jianju
            self._wangge[i][3] = 100 * i / (self._n - 1)
            self._wangge[i][4] = np.round((self._wangge[i][1] - jz) * 100 / jz, 2)


class simpleWange(wangGebase):
    pass
