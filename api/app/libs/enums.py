# _*_ coding: utf-8 _*_
# @Time : 2019/4/12 19:53
# @Author : lorenzo
from enum import  Enum

#表示客户端类型
class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    #微信小程序
    USER_MINA = 200

    #微信公众号
    USER_WX = 201
    pass