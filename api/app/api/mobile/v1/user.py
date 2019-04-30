# _*_ coding: utf-8 _*_
# @Time : 2019/4/11 19:39
# @Author : lorenzo
from app.libs.redprint import Redprint
from  flask import jsonify
from app.libs.error_code import NotFound

api = Redprint('user')


@api.route('/get',methods=['GET'])
def getUser():
    data={'code':'200','data':{"list":[{"name":'1',"age":"18"},{"name":'1',"age":"28"},{"name":'w1',"age":"18"}],"list2":{"name":'1',"age":"38"}}}
    list=data
    return jsonify(list)