#!/usr/bin/env python

# encoding: utf-8

'''
@Copyright (C), LiXiangping
@version:
@release:
@author: LiXiangping
@email: 752070569@qq.com
@file: user_service.py
@time: 2018/5/24 0024 上午 11:03
@description:
'''


from model.user import User, Friend, Group
import hashlib

class UserService:


    @staticmethod
    def create_friend_table(tablename, metadata):
        Friend.create_friend_table(tablename, metadata)

    @staticmethod
    def create_group_table(groupname, metadata):
        Group.create_group_table(groupname, metadata)

    @staticmethod
    def hashmd5(password):
        s = hashlib.md5()
        s.update(password.encode('utf-8'))
        return s.hexdigest()

    def get_user(self, db_session, userid):
        return db_session.query(User).filter(User.userid == userid).first()


    def update_user_info(self, db_session, userid, password, user):
        '''更新信息，用户名或者email'''
        current_user = self.get_user(db_session, userid)
        if current_user and current_user.password == password:
            if 'username' in user:
                current_user = user.username
            if 'email' in user:
                current_user = user.email
            db_session.commit()
            return current_user
        else:
            return None

    @staticmethod
    def update_user_password(db_session,userid, new_password, old_password):
        count = db_session.query(User).filter(User.userid == userid, User.password == old_password)\
            .update({'password': new_password})
        return count

    @staticmethod
    def save_user(db_session, user, userid):
        userinfo = User(username=user.username,
                        password=user.password,
                        email=user.email,
                        userid=userid + 1)
        db_session.add(userinfo)
        db_session.commit()
        return userinfo


    def save_friend(self):
        pass


    def get_friends(self, db_session, userid):
        pass

    def get_groups(self, db_session, userid):
        pass
