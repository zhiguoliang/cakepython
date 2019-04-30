# _*_ coding: utf-8 _*_
# @Time : 2019/4/11 18:30
# @Author : lorenzo

#封装flask对象
from flask import Flask

#注册蓝图
def register_blueprints(app):

    #移动端注册蓝图
    from app.api.mobile  import  create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1/mobile')


    #后台管理系统注册蓝图
    from  app.api.admin import create_blueprint_admin_v1
    app.register_blueprint(create_blueprint_admin_v1(), url_prefix='/v1/admin')



def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprints(app)
    return app
