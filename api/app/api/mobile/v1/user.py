# _*_ coding: utf-8 _*_
# @Time : 2019/4/11 19:39
# @Author : lorenzo
from flask import request, jsonify

from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
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


#总分



