# _*_ coding: utf-8 _*_
# @Time : 2019/4/11 19:39
# @Author : lorenzo
from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from flask import request

from app.validators.forms import ClientForm

api = Redprint('client')

@api.route('/register')
def create_client():
    data = request.json
    form = ClientForm()

    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL:__register_user_by_email,
            ClientTypeEnum.USER_NINA:__register_user_by_NINA
        }

    #request.args.to_dict()
    #登录，注册
    #参数 校验 接收参数
    #WTForms校验
    return '1dsadsadsadasdsd'


def __register_user_by_email():
    pass


def __register_user_by_NINA():
    pass