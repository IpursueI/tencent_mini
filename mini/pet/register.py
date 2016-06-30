#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import util
import json
import hashlib
import datetime
'''
chayfan:注册时赋token,tokenoverdue字段初始值
tokenoverdue字段由userid+userpassword+当日日期，再经过md5加密获得
'''
def register(data):
    try:
        userId = data["user_id"]
    except KeyError:
        return util.errorJsonWrapper("注册数据没有user_id字段")

    try:
        userPassword = data["user_password"]
    except KeyError:
        return util.errorJsonWrapper("注册数据没有user_id字段")
    try:
        userPassword = hashlib.md5(userPassword).hexdigest()

        token = hashlib.md5(userId + userPassword + str(datetime.datetime.now())).hexdigest()

        tokenoverdue = str(datetime.datetime.now() + datetime.timedelta(days = 3))

        checkRes = models.User.objects.filter(user_id=userId)
    except:
        return util.errorJsonWrapper("test")

    if len(checkRes) == 0:
        try:
            tmpUser = models.User(user_id = userId, user_password = userPassword, user_token = token, user_token_overdue = tokenoverdue)
            tmpUser.save()
        except Exception:
            return util.errorJsonWrapper("register 数据写入数据库出错")

        retValueItem = {}
        retValueItem['user_token'] = token
        retValueItem["user_nickname"] = ""
        retValueItem["user_avatar"] = ""
        retValueItem["user_address"] = ""
        retValueItem["user_age"] = 0
        retValueItem["user_interest"] = 0
        retValueItem["user_gender"] = 0
        retValueItem["user_authenticated"] = False
        res = dict(retCode=0, retMsg="", retValue = retValueItem)

        return json.dumps(res)
    else:
        return util.errorJsonWrapper("注册失败，该手机号已经被注册")
