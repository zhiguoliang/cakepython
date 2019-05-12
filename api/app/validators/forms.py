# _*_ coding: utf-8 _*_
# @Time : 2019/4/12 19:59
# @Author : lorenzo

from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError
from app.libs.enums import ClientTypeEnum
from app.models.user import User


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), length(
        min=5,max=32
    )])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])
    def validate_type(self, value):
      try:
        client = ClientTypeEnum(value.data)
      except ValueError as e :
          raise e

      self.type.daya = client


#针对email注册的规则

class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='invalidate email')
    ])

    secret = StringField(validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(), length(min=2, max=22)])

    #验证账号是否被验证过
    def validate_account(self,value):
       if User.query.filter_by(email=value.data).first():
           raise ValidationError