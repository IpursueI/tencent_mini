#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import util
import json
import hashlib
'''
chayfan:通过token验证用户身份
'''
RECOMMEND_FUNC = 1
FILTER_FUNC = 2

DEFAULT_RECOM = 0
PRICE_RECOM = 1
INTEREST_RECOM = 2

GENDER_ALL = 0
GENDER_MALE = 1
GENDER_FEMALE = 2

PET_ALL = 0
PET_CAT = 1
PET_DOG = 2
PET_RABBIT = 3

def getInfoList(data):
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
        functionType = data["function_type"]
    except KeyError:
        return util.errorJsonWrapper("请求数据没有function_type字段")
    try:
        number = data["number"]
    except KeyError:
        return util.errorJsonWrapper("请求数据没有number字段")
    try:
        recommend_Type = data["recommend_type"]
    except KeyError:
        return util.errorJsonWrapper("请求数据没有recommend_type字段")
    try:
        gender = data["gender"]
    except KeyError:
        return util.errorJsonWrapper("请求数据没有gender字段")
    try:
        petType = data["pet_type"]
    except KeyError:
        return util.errorJsonWrapper("请求数据没有pet_type字段")

    #resList = models.Participant.objects.all()

    if functionType == RECOMMEND_FUNC:
        if recommend_Type == DEFAULT_RECOM:
            resList = models.Participant.objects.filter(participant_user_type=1)
        else:
            resList = intelligentSort(userId, recommend_Type)

    elif functionType == FILTER_FUNC:
        if gender == GENDER_ALL and petType == PET_ALL:
            resList = models.Participant.objects.filter(participant_user_type=1)
        elif gender == GENDER_ALL:
            resList = models.Participant.objects.filter(participant_activity__activity_pet_type=pet_type,participant_user_type=1)
        elif petType == PET_ALL:
            resList = models.Participant.objects.filter(participant_user__user_gender=gender,participant_user_type=1)
        else:
            resList = models.Participant.objects.filter(participant_activity__activity_pet_type=petType,participant_user__user_gender=gender,participant_user_type=1)            

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

def intelligentSort(userId, sortType):
        user = models.User.objects.filter(user_id = userId).first()
        if not user:
            return []

        if sortType == PRICE_RECOM:
            partList = models.Participant.objects.order_by('participant_activity__activity_price')
            partListNew = []
            for part in partList:
                if part.participant_user_type == 1:
                    partListNew.append(part)
            return partListNew

        elif sortType == INTEREST_RECOM:
            tag = user.user_interest
            partList = models.Participant.objects.filter(participant_user_type=1)
            tagDiff = 0
            recommendDict = {}
            for participant in partList:
                recommendDict[participant] = str(bin(tag^participant.participant_user.user_interest)).count("1")
            sortedList = sorted(recommendDict.items(), lambda x, y:cmp(x[1],y[1]))
                                                                                                                        
            return [item[0] for item in sortedList]                                                        
