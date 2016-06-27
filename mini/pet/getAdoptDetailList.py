#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import datetime
import util
import json
import hashlib

'''
获取详细收养信息, by stanwu 2016/06/26
post参数名：method
post参数内容：{"name":"getAdoptDetailList","args":{"activity_id":xxx, "user_token" : "xxx"}}

token用作身份验证,token验证错误，则无法访问

服务器返回值(json格式)：
    请求失败：
    {"retValue": "", "retCode": -1, "retMsg": "xxxxx"}
    请求成功：
    {"retValue":[{"user_id","xxx", "activity_picture":xxx, "user_avatar":xxx, "user_nickname":"xxx",
	"user_age":xxx, "user_interest":xxx, "activity_pet_type":xxx, "activity_price":xxx,
	"activity_address":"xxx", "activity_introduction":"xxx","activity_start_time":"xxx",
	"activity_end_time":"xxx"}],
 	"retCode": 0,
 	"retMsg": ""}
'''

def getAdoptDetailList(data):

    activityId = data.get("activity_id")
    if not activityId:
        return util.errorJsonWrapper("收养详细信息获取请求错误,不存在该activity_id")

    activity = models.Activity.objects.get(pk = activityId)
    if not activity:
        return util.errorJsonWrapper("收养详细信息获取请求错误,不存在该活动")

    user = models.Participant.objects.filter(participant_activity = activity).first().participant_user
    if not user:
        return util.errorJsonWrapper("收养详细信息获取请求错误,不存在该用户")

    # check token by stanwu 为了方便调试暂时注释掉
    #token = data.get("user_token")
    #if token != user.user_token:
    #    return util.errorJsonWrapper("token错误")

    detailDict = {  "user_id" : user.user_id, "activity_picture" : activity.activity_picture, "user_avatar" : user.user_avatar,
                    "user_nickname" : user.user_nickname, "user_age" : user.user_age, "user_interest" : user.user_interest,
                    "activity_pet_type" : activity.activity_pet_type, "activity_price" : activity.activity_price,
                    "activity_address": activity.activity_address, "activity_introduction": activity.activity_introduction,
                    "activity_start_time": activity.activity_start_time,
                    "activity_end_time": activity.activity_end_time
                    }

    retList = []
    retList.append(detailDict)
    res = dict(retCode = 0, retMsg = "", retValue = detailDict)

    return json.dumps(res)


