#!/usr/bin/env python

# encoding: utf-8

'''
@Copyright (C), LiXiangping
@version:
@release:
@author: LiXiangping
@email: 752070569@qq.com
@file: user.py
@time: 2018/5/22 0022 下午 5:37
@description:
'''

from model.base import DbBase, DbInit
from sqlalchemy.orm import contains_eager, deferred
from sqlalchemy import Column, Integer, String, TEXT, DATETIME, Boolean, ForeignKey

class User(DbBase, DbInit):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(length=64), unique=True, index=True)
    password = Column(String(length=128))
    email = Column(String(length=64), unique=True, index=True)

