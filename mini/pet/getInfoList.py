#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import util
import json
import hashlib
'''
chayfan:通过token验证用户身份
'''
def getInfoList(data):

    MAINPAGE = 1
    ALLADOPTLIST = 2
    ALLFOSTERLIST = 3
    USERADOPTLIST = 4
    USERFOSTERLIST = 5

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

    if activityType == MAINPAGE or activityType == ALLADOPTLIST:
        resList = util.intelligentSort(userId, sortType)
    elif activityType == ALLFOSTERLIST: 
        resList = models.Participant.objects.filter(participant_user_type=2)
    elif activityType == USERADOPTLIST: 
        resList = models.Participant.objects.filter(participant_user__user_id=userId, participant_user_type=1)
    elif activityType == USERFOSTERLIST: 
        resList = models.Participant.objects.filter(participant_user__user_id=userId, participant_user_type=2)

    try:
        retValue = []
        for item in resList:
            retValueItem = {}
            userInfo = item.participant_user
            activityInfo = item.participant_activity

            retValueItem["activity_id"] = activityInfo.pk
            retValueItem["activity_picture"] = activityInfo.activity_picture
            retValueItem['activity_address'] = activityInfo.activity_address
            retValueItem['activity_price'] = activityInfo.activity_price
            retValueItem['activity_introduction'] = activityInfo.activity_introduction
            retValueItem['activity_pet_type'] = activityInfo.activity_pet_type
            retValueItem['activity_start_time'] = activityInfo.activity_start_time
            retValueItem['activity_end_time'] = activityInfo.activity_end_time
            

            retValueItem["user_id"] = userInfo.user_id
            retValueItem["user_nickname"] = userInfo.user_nickname
            retValueItem["user_avatar"] = userInfo.user_avatar
            retValueItem["user_address"] = userInfo.user_address
            retValueItem["user_age"] = userInfo.user_age
            retValueItem["user_interest"] = userInfo.user_interest
            retValueItem["user_gender"] = userInfo.user_gender
            retValueItem["user_authenticated"] = userInfo.user_authenticated

            retValue.append(retValueItem)

        if number >= 0:
            retValue = retValue[:number]

        result = {}

        result["retValue"] = retValue
        result["retCode"] = 0
        result["retMsg"] = ""

        return json.dumps(result)
    except Exception:

        return util.errorJsonWrapper("请求信息列表失败")
