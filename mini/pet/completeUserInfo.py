#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import util
import json
import hashlib

def completeUserInfo(data):
    try:
        userId = data["user_id"]
    except KeyError:
        return util.errorJsonWrapper("注册数据没有user_id字段")

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
        userAvatar = data["user_avatar"]
    except KeyError:
        return util.errorJsonWrapper("注册数据没有user_avatar字段")
    try:
        userNickname = data["user_nikename"]
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
            FIllin.user_avatar = userAvatar
            FIllin.user_nikename = userNickname
            FIllin.user_longtitude = userLongtitude
            FIllin.user_latitude = userLatitude
            FIllin.user_interest = userInterest

            FIllin.save()

        except Exception:
            return util.errorJsonWrapper("fillinfo 数据写入数据库出错")

        return util.simpleOkJsonWrapper()
    else:
        return util.errorJsonWrapper("该用户不存在")