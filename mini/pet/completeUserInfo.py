#-*- coding:UTF-8 -*-
import os
import sys
from django.http import HttpResponse
import models
import util
import json
import hashlib
import time
from django.conf import settings

def completeUserInfo(data, files):
    try:
        userId = data["user_id"]
    except KeyError:
        return util.errorJsonWrapper("注册数据没有user_id字段")
    try:
        userToken = data["user_token"]
    except KeyError:
        return util.errorJsonWrapper("注册数据没有user_token字段")

    if not util.checkToken(userId, userToken):
        return util.errorJsonWrapper("token 验证失败")

    try:
        userGender = data["user_gender"]
    except KeyError:
        return util.errorJsonWrapper("注册数据没有user_gender字段")
    try:
        userAge = data["user_age"]
    except KeyError:
        return util.errorJsonWrapper("注册数据没有user_age字段")
    try:
        userAddress = data["user_address"]
    except KeyError:
        return util.errorJsonWrapper("注册数据没有user_address字段")
    try:
        userNickname = data["user_nickname"]
    except KeyError:
        return util.errorJsonWrapper("注册数据没有user_nickname字段")
    try:
        userInterest = data["user_interest"]
    except KeyError:
        return util.errorJsonWrapper("注册数据没有user_interest字段")
    

    FIllin = models.User.objects.get(user_id=userId)

    if FIllin:
        try:
            FIllin.user_gender = userGender
            FIllin.user_age = userAge
            FIllin.user_address = userAddress
            FIllin.user_nickname = userNickname
            FIllin.user_interest = userInterest
            
            picName = util.savePicture(files,"user_avatar",2*1024*1024)
            if picName == -1:
                return util.errorJsonWrapper("failed")
            if picName != "":
                FIllin.user_avatar = picName 

            FIllin.save()

        except Exception:
            return util.errorJsonWrapper("用户数据写入数据库出错")

        return util.simpleOkJsonWrapper()

    else:
        return util.errorJsonWrapper("该用户不存在")
