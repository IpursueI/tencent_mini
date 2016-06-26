#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import util
import json
import hashlib

def getInfoList(data):
    try:
        userId = data["user_id"]
    except KeyError:
        return util.errorJsonWrapper("请求数据没有user_id字段")

    try:
        activityType = data["activity_type"]
    except KeyError:
        return util.errorJsonWrapper("请求数据没有activity_type字段")

    try:
        number = data["number"]
    except KeyError:
        return util.errorJsonWrapper("请求数据没有number字段")

    try:
        sortType = data["sort_type"]
    except KeyError:
        return util.errorJsonWrapper("请求数据没有sort_type字段")
    
    resList = models.Participant.objects.filter(participant_user__user_id=userId, participant_user_type=activityType)

    retValue = []
    for item in resList:
        retValueItem = {}
        userInfo = item.participant_user
        activityInfo = item.participant_activity

        retValueItem["activity_id"] = activityInfo.pk
        retValueItem["activity_picture"] = activityInfo.activity_picture
        retValueItem['activity_price'] = activityInfo.activity_price

        retValueItem["user_nickname"] = userInfo.user_nickname
        retValueItem["user_avatar"] = userInfo.user_avatar
        retValueItem["user_address"] = userInfo.user_address

        retValue.append(retValueItem)

    retValue = retValue[:number]

    result = {}

    result["retValue"] = retValue
    result["retCode"] = 0
    result["retMsg"] = ""

    return json.dumps(result)
