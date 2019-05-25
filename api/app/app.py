# _*_ coding: utf-8 _*_
# @Time : 2019/4/11 18:30
# @Author : lorenzo

#封装flask对象
from datetime import date

from flask import Flask as _Flask
from flask.json import  JSONEncoder  as _JSONEncoder

#对序列化的jsonify源代码改写
from app.libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
           return  dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder



