# _*_ coding: utf-8 _*_
# @Time : 2019/4/11 19:39
# @Author : lorenzo
from app.libs.enums import ClientTypeEnum
from app.libs.error import APIException
from app.libs.redprint import Redprint
from flask import jsonify, request
from app.libs.error_code import NotFound, ClientTypeError, Success
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm


api = Redprint('client')

@api.route('/register',methods=['POST'])
def create_client():

    form = ClientForm().validata_for_api()

    promise = {
                    ClientTypeEnum.USER_EMAIL: __register_user_by_email
                }
    print(form.type.data)
    promise[form.type.data]()
    data = [{'name':'lorenzo','age':'1'}]
    #我们可以接受定义的复杂，但不能接受调用的时候的复杂
    return Success(result=data)


def __register_user_by_email():

    form = UserEmailForm().validata_for_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)


def __register_user_by_NINA():
    pass