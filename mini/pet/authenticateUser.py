#-*- coding:UTF-8 -*-
import os
import sys
from django.http import HttpResponse
import models
import util
import json
from django.conf import settings

def authenticateUser(data, files):
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

    user = models.User.objects.get(user_id=userId)

    if user:
        try:
            picName = util.savePicture(files,"user_authenticated_picture",20*1024*1024)
            if picName == -1:
                return util.errorJsonWrapper("failed")
            user.user_authenticated_picture = picName 
            user.user_authenticated = True
            user.save()

        except Exception:
            return util.errorJsonWrapper("用户认证信息存入数据库出错")

        return util.simpleOkJsonWrapper("用户认证成功")
    else:
        return util.errorJsonWrapper("该用户不存在")
