# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:00:44 2017

@author: 久久为功
"""
import datetime
import sys

def LogAll(caller):
    def wrapper(fun):
        '''执行过程屏幕上的输出,都存在文件中，且程序异常及原因也会存在文件里'''
        def rf():
            now=datetime.datetime.now()
            str_date=now.strftime('%Y%m%d')
            Log_File_Name='%s_Log_%s.txt' %(caller,str_date)
            f=open(Log_File_Name,'a')
            sys.stdout=f
            sys.stderr=f
            try:
                return fun()
            except:
                f.close()
            finally:
                f.close()
        return rf
    return wrapper
