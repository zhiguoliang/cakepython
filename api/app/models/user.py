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
from sqlalchemy import Column, Integer, String,db


class User(db.Model):
    __tablename__="user"
    id = db.Column(db.Integer(), primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24))



