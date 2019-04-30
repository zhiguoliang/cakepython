# _*_ coding: utf-8 _*_
# @Time : 2019/4/11 19:17
# @Author : lorenzo
from flask import Blueprint
from app.api.mobile.v1 import user, client


def create_blueprint_v1():
    #实例化一个蓝图对象

     mobile = Blueprint('mobile',__name__)

     #注册移动端模块宏图
     user.api.register(mobile)
     client.api.register(mobile)

     return mobile