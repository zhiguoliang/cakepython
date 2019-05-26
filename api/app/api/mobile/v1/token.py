#!/user/bin/env python
#coding=utf-8

'''
@author: lorenzo
@Wechat cake project
@project: api
@file: token.py
@time: 2019/5/25 12:42
@desc:
'''
from flask import current_app, jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm
from itsdangerous import  TimedJSONWebSignatureSerializer as Serializer


api = Redprint('token')

@api.route('', methods=['POST'])
def get_token():
    print('1111')
    form = ClientForm().validata_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify
    }
    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )

    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(
        identity['uid'],
        form.type.data,
        identity['scope'],
        expiration
    )

    t = {
        'token':token.decode('ascii')
    }

    return  Success(result=t)


    #生成令牌 Token

def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """生成令牌"""
    s = Serializer(current_app.config["SECRET_KEY"], expires_in=expiration)

    return  s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope':scope
    })

