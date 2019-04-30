# _*_ coding: utf-8 _*_
# @Time : 2019/4/11 19:17
# @Author : lorenzo
from flask import Blueprint

from app.api.admin.v1 import index

def create_blueprint_admin_v1():
    #实例化一个蓝图对象

     admin = Blueprint('admin',__name__)
     #注册pc端模块宏图
     index.api.register(admin)


     return admin