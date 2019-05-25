#!/user/bin/env python
#coding=utf-8

'''
@author: lorenzo
@Wechat cake project
@project: api
@file: base.py
@time: 2019/5/19 12:25
@desc:
'''
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        data = request.json
        super(BaseForm,self).__init__(data=data)



    def validata_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self

