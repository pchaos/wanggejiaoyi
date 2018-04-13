# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File    : tools.py

Description :

@Author :       pchaos

date：          18-4-11
-------------------------------------------------
Change Activity:
               18-4-11:
@Contact : p19992003#gmail.com                   
-------------------------------------------------
"""
__author__ = 'pchaos'

import os,sys
import shutil
import pandas as pd
import subprocess as sub
import shlex
import json

def shell_exec(cmd):
	print("[Command]"+cmd)
	sys.stdout.flush()
	c=os.popen(cmd).read()
	return c.strip()
def passthru(cmd):
	#print os.popen(cmd).read()
	#sys.stdout.flush()
    #sub.call(shlex.split(cmd),stdout=sys.stdout)
	print("[Command]"+cmd)
	sys.stdout.flush()
	sub.call(cmd,shell=True,stdout=sys.stdout)

def mv(src,dest):
	shell_exec("mv %s %s"%(src,dest))
def cp(src,dest):
	shell_exec("cp %s %s -r "%(src,dest))
def head(src,n=1):
    return shell_exec("head -%d %s"%(n,src))
def tail(src,n=1):
    return shell_exec("tail -%d %s"%(n,src))

def cd(path):
	os.chdir(path)

def pwd():
	return os.getcwd()

def ls(path='*'):
	import glob
	return glob.glob(path)

def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False

def mkcd(path):
    mkdir(path)
    cd(path)
def exists(path):
    return os.path.exists(path)

def dirname(path):
    return os.path.dirname(path).strip()

def exit(info='Exited by user!'):
	print(info)
	sys.stdout.flush()
	sys.exit();


def read(fileName):
    file = open(fileName);
    s = file.read()
    file.close();
    return s


def write(cmd, fileName, mode="w", sep=""):
    file = open(fileName, mode);
    file.write(str(cmd) + sep);
    file.close();


def loadjson(file):
    return json.loads(read(file))


def parseyaml(filename):
    try:
        import yaml
    except ImportError:
        print("You need to install python-yaml.")
        exit(1)

    try:
        from yaml import CLoader as Loader
        from yaml import CDumper as Dumper
    except ImportError:
        from yaml import Loader, Dumper
    string = open(filename).read()
    data = yaml.load(string, Loader=Loader)
    return data

def debug(cmd):
    write(str(cmd),'debug.txt','a',sep="\n")

def to_txt(columns,data,filename):
	quants=pd.DataFrame(data,columns =columns)
	quants.to_csv(filename,sep='\t',index=None)
