#!/usr/bin/env python

# encoding: utf-8

'''
@Copyright (C), LiXiangping
@version:
@release:
@author: LiXiangping
@email: 752070569@qq.com
@file: user_utils.py
@time: 2018/5/24 0024 上午 11:45
@description:
'''


def get_friendtable_name(userid):
    '''好友表'''
    return 'friend_%d'%userid

def get_grouptable_name(userid):
    '''群表'''
    return 'group_%d'%userid

