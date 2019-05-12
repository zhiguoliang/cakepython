# _*_ coding: utf-8 _*_
# @Time : 2019/4/11 19:39
# @Author : lorenzo
from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from flask import jsonify, request
from app.libs.error_code import NotFound
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('user')


@api.route('/get',methods=['GET'])
def getUser():
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL:__register_user_by_email()
        }
        promise[form.type.data]
    return 'success'

#总分


def __register_user_by_email():
    form =UserEmailForm(data = request.json)
    if form.validate():
       User.register_by_email(form.nickname.data,form.account.data,form.secret.data)