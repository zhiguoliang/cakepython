# _*_ coding: utf-8 _*_
# @Time : 2019/4/11 19:39
# @Author : lorenzo
from flask import request, jsonify, g

from app.libs.error_code import Success, DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = Redprint('user')


@api.route('', methods=['GET'])
@auth.login_required
def getUser():
    #token 1个月 2小时
    #token 是否过期 是否合法
    #token
    uid = request.args.get('uid')
    user = User.query.get_or_404(uid)

    return Success(result = user)

@api.route('/get', methods=['GET'])
@auth.login_required
def super_get_User():
    #token 1个月 2小时
    #token 是否过期 是否合法
    #token
    uid = request.args.get('uid')
    user = User.query.get_or_404(uid)

    return Success(result = user)

#总分

#删除用户模型
@api.route('/delete',methods=['DELETE'])
@auth.login_required
def delete_uer():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()

#管理员删除用户
@api.route('/superDelete',methods=['DELETE'])
def super_delete_user():
    uid = request.args.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()

