#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import util
import json
import hashlib
import datetime

def logout(data):

    try:
        userId = data["user_id"]
    except KeyError:
        return util.errorJsonWrapper("请求数据没有user_id字段")
    try:
        userToken = data["user_token"]
    except KeyError:
        return util.errorJsonWrapper("请求数据没有token字段")

    if not util.checkToken(userId, userToken):
        return util.errorJsonWrapper("token 验证失败")

    user = models.User.objects.filter(user_id = userId).first()

    if not user:
        return util.errorJsonWrapper("不存在该用户名")
    else:
        user.user_token_overdue = str(datetime.datetime.now())
        user.save()
        return util.simpleOkJsonWrapper()
