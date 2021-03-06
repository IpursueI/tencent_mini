#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import util
import json
import hashlib
import datetime
import time
'''
登陆功能：by stanwu, 2016/06/25

post参数名：method
post参数内容：{"name":"login", "args":{"user_id":"15666666666", "user_password":"123"}}

服务器返回值(json格式):
    注册成功：
    {"retValue": "", "retCode": 0, "retMsg": ""}
    注册失败：
    {"retValue": "", "retCode": -1, "retMsg": "xxxxx"}

chayfan修改: 加入token验证，若token过期，进行密码登录，同时更新token值与tokenoverdue值
'''
def login(data):
    userID = data.get("user_id")
    token = data.get("user_token")
    password = data.get("user_password")
    user = models.User.objects.filter(user_id = userID).first()

    if not user:
        return util.errorJsonWrapper("不存在该用户名")
    else:
        if token:
            if str(datetime.datetime.now()) < user.user_token_overdue:
                if token == user.user_token:
                    return getUserInfo(user,token)
                else:
                    return util.errorJsonWrapper("token错误")
            else:
                return util.errorJsonWrapper("token已过期")
        else:
            if user.user_password != hashlib.md5(password).hexdigest():
                return util.errorJsonWrapper("密码错误")
            else:
                token = hashlib.md5(userID + password + str(datetime.datetime.now())).hexdigest()
                user.user_token = token
                user.user_token_overdue = str(datetime.datetime.now() + datetime.timedelta(days = 3))
                user.save()
                
                return getUserInfo(user, token)

def getUserInfo(user, token):
    retValueItem = {}
    retValueItem['user_token'] = token
    retValueItem["user_nickname"] = user.user_nickname
    retValueItem["user_avatar"] = user.user_avatar
    retValueItem["user_address"] = user.user_address
    retValueItem["user_age"] = user.user_age
    retValueItem["user_interest"] = user.user_interest
    retValueItem["user_gender"] = user.user_gender
    retValueItem["user_authenticated"] = user.user_authenticated
    res = dict(retCode=0, retMsg="", retValue = retValueItem)

    return json.dumps(res)
