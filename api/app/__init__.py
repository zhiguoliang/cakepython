# _*_ coding: utf-8 _*_
# @Time : 2019/4/11 18:29
# @Author : lorenzo
#注册蓝图
from app.app import Flask


def register_blueprints(app):

    #移动端注册蓝图
    from app.api.mobile  import  create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1/mobile')


    #后台管理系统注册蓝图
    from  app.api.admin import create_blueprint_admin_v1
    app.register_blueprint(create_blueprint_admin_v1(), url_prefix='/v1/admin')

#注册flask-sqlachemy
def register_plugin(app):
    from app.models.base import db
    db.init_app(app)

    with app.app_context():
     db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprints(app)
    register_plugin(app)
    return app