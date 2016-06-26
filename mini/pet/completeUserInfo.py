#-*- coding:UTF-8 -*-
import os
import sys
from django.http import HttpResponse
import models
import util
import json
import hashlib
import mini.settings
import time
sys.path.append("..")

def completeUserInfo(data, files):
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
            FIllin.user_nikename = userNickname
            #FIllin.user_longitude = userLongitude
            #FIllin.user_latitude = userLatitude
            FIllin.user_interest = userInterest
            
            #保存头像
            FIllin.user_avatar = saveUserAvatar(files)

            FIllin.save()

        except Exception:
            return util.errorJsonWrapper("用户数据写入数据库出错")

        return util.simpleOkJsonWrapper()

    else:
        return util.errorJsonWrapper("该用户不存在")


def saveUserAvatar(files):
    if files:  #如果该request携带文件数据
        try:
            avatar = files["user_avatar"] #图像的key
        except Exception:
            return util.errorJsonWrapper("没有头像文件")

        filePath = os.path.join(settings.MEDIA_ROOT,time.strftime("%Y%m%d%H%M%S")+avatar.name)
       
        with open(filePath) as destination:
            for chunk in avatar.chunks():
                destination.write(chunk)

        return filePath
    else:
        return ""
