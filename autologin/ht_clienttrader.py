# -*- coding: utf-8 -*-
"""
-------------------------------------------------

@File    : ht_clienttrader.py.py

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

# coding:utf8

import pywinauto
import pywinauto.clipboard
import time
import platform

from .clienttrader import ClientTrader

class HTClientTrader(ClientTrader):
    @property
    def broker_type(self):
        return 'ht'

    def login(self, user, password, exe_path, comm_password=None, **kwargs):
        """
        :param user: 用户名
        :param password: 密码
        :param exe_path: 客户端路径, 类似
        :param comm_password:
        :param kwargs:
        :return:
        """
        if comm_password is None:
            raise ValueError('华泰必须设置通讯密码')

        try:
            self._app = pywinauto.Application().connect(
                path=self._run_exe_path(exe_path), timeout=2)
        except Exception:
            self._app = pywinauto.Application().start(exe_path)

            # wait login window ready
            while True:
                try:
                    self._app.top_window().Edit1.wait('ready')
                    break
                except RuntimeError:
                    pass

            time.sleep(1)
            if  platform.release() == 'XP':
                # windows xp系统输入需要延迟等待. xp系统放弃，无法保证输入正确
                delaysec= 1
            else:
                delaysec = 0.05
            self._app.top_window().Edit1.Click()
            if (self._app.top_window().Button4.GetCheckState() == 0 or
                len(self._app.top_window().Edit1.WindowText()) < 8):
                # 如果有勾选保存账号则跳过输入账号
                self._app.top_window().Edit1.type_keys(user)
                time.sleep(delaysec)
            self._app.top_window().Edit2.Click()
            self._app.top_window().Edit2.type_keys(password)
            time.sleep(delaysec)
            self._app.top_window().Edit1.Click()
            self._app.top_window().Edit3.type_keys(comm_password)
            time.sleep(delaysec)
            self._app.top_window().button0.click()

            # detect login is success or not
            self._app.top_window().wait_not('exists', 10)

            self._app = pywinauto.Application().connect(
                path=self._run_exe_path(exe_path), timeout=10)
        self._close_prompt_windows()
        self._main = self._app.window(title='网上股票交易系统5.0')

    @property
    def balance(self):
        self._switch_left_menus(self._config.BALANCE_MENU_PATH)

        return self._get_balance_from_statics()

    def _get_balance_from_statics(self):
        result = {}
        for key, control_id in self._config.BALANCE_CONTROL_ID_GROUP.items():
            result[key] = float(
                self._main.window(
                    control_id=control_id,
                    class_name='Static',
                ).window_text())
        return result
