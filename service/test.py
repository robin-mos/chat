#!/usr/bin/env python

# encoding: utf-8

'''
@Copyright (C), LiXiangping
@version:
@release:
@author: LiXiangping
@email: 752070569@qq.com
@file: test.py
@time: 2018/5/24 0024 下午 4:25
@description:
'''

from model.base import DbBase
from base import db
from model.user import User
from service import user_utils
from service.user_service import UserService
import base

def user():
    userid = 8000001
    print(UserService.hashmd5('123456'))

    user = User(
        userid=userid,
        username='testname1',
        password=UserService.hashmd5('123456'),
        email='12345678@qq.com',
    )
    UserService.save_user(db(), user, userid)
    UserService.create_friend_table(user_utils.get_friendtable_name(userid+1), DbBase.metadata)
    UserService.create_group_table(user_utils.get_grouptable_name(userid+1), DbBase.metadata)
    DbBase.metadata.create_all(bind=base.engine)


if __name__ == '__main__':
    # DbBase.metadata.create_all(base.engine)
    # user()
    person = dict(name='lee',email='')
    if 'name' in person:
        print('name')
    if 'password' in person:
        print('nnnnn')
    if 'email' in person:
        print('email')