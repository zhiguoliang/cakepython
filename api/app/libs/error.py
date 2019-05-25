#!/user/bin/env python
#coding=utf-8

'''
@author: lorenzo
@Wechat cake project
@project: api
@file: error.py
@time: 2019/4/18 15:06
@desc:
'''

from flask  import request, json
from werkzeug.exceptions import HTTPException

class APIException(HTTPException):
    code = 500
    msg = 'sorry,we make mistake'
    error_code = 999
    result =[]
    def __init__(self, msg=None, code=None,error_code=None,headers=None,result=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        if result:
            self.result = result
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg = self.msg,
            error_code = self.error_code,
            result = self.result,
            request=request.method + ''+self.get_url_no_param()
        )
        text = json.dumps(body)

        return text

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')[0]
        return main_path