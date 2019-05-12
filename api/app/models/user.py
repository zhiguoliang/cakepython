#!/user/bin/env python
#coding=utf-8

'''
@author: lorenzo
@Wechat cake project
@project: api
@file: user.py
@time: 2019/4/18 12:57
@desc:
'''
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash

from app.models.base import Base,db


class User(Base):
    __tablename__="user"
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24))
    auth = Column(SmallInteger, default=1)
    _password= Column('password',String(100))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname,account,secret):
        with db.auth_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)
            pass


