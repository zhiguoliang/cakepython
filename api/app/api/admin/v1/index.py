# _*_ coding: utf-8 _*_
# @Time : 2019/4/11 19:39
# @Author : lorenzo
from app.libs.redprint import Redprint

api = Redprint('index')


@api.route('/get')
def adminUser():
    return '2'


@api.route('/create')
def create():
    return '21111'