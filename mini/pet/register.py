#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import util
import json
import hashlib

def register(data):
    try:
        userId = data["user_id"]
    except KeyError:
        return util.errorJsonWrapper("注册数据没有user_id字段")

    try:
        userPassword = data["user_password"]
    except KeyError:
        return util.errorJsonWrapper("注册数据没有user_id字段")

    userPassword = hashlib.md5(userPassword).hexdigest()
    tmpUser = models.User(user_id = userId, user_password = userPassword)
    tmpUser.save()
    return util.simpleOkJsonWrapper()
