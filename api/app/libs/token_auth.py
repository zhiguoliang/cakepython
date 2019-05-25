#!/user/bin/env python
#coding=utf-8

'''
@author: lorenzo
@Wechat cake project
@project: api
@file: token_auth.py
@time: 2019/5/25 14:28
@desc:
'''
from flask import current_app, g
from flask_httpauth import  HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from sqlalchemy.util import namedtuple

from app.libs.error_code import AuthFailed

#定义一个对象来存储数据
User = namedtuple('User',['uid','ac_type','scope'])



auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(token,password):
    #key = Authorization
    #value = basic base64(lorenzo:12345678)

    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        g.user = user_info
    return True

def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    #验证token是否异常
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)
    #验证token是否过期
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', error_code=1003)

    uid = data['uid']
    ac_type = data['type']

    return  User(uid, ac_type, '')