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
            
            #保存头像地址
            FIllin.user_avatar = saveUserAvatar(files)
            #return util.errorJsonWrapper(saveUserAvatar(files))

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
            avatarSavedName = time.strftime("%Y%m%d%H%M%S")+avatar.name
            filePath = os.path.join(settings.MEDIA_ROOT,avatarSavedName)
       
            with open(filePath, 'wb+') as destination:
                for chunk in avatar.chunks():
                    destination.write(chunk)
        except:
            return ""

        avatarUrl = "media/"+avatarSavedName
        return avatarUrl
    else:
        return ""
