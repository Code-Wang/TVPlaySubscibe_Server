#!/usr/bin/env Python
# coding=utf-8
import configparser

def getConfig(hkey,key):
    cf = configparser.ConfigParser()
    cf.read("/home/wangyaobo/Github/TVPlaySubscibe_Server/config/database.conf")
    if key=="port":
        result = cf.getint(hkey, key)
    else:
        result = cf.get(hkey, key)
    return result
