#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import datetime
import util
import json
import hashlib

'''
发布收养信息：by stanwu, 2016/06/25
post参数名：method
post参数内容：
	{"name":"issueAdoptPetInfo","args":{"user_id":"xxx","activity_picture":xxx, "activity_introduction":"xxx",
 	"activity_address":"xxx","activity_longitude":"xxx","activity_latitude":"xxx",
	"activity_pet_type":xxx,"activity_price":xxx,
	"activity_start_time":"xxx", "activity_end_time":"xxx"}}

服务器返回值(json格式):
    注册成功：
    {"retValue": "", "retCode": 0, "retMsg": ""}
    注册失败：
    {"retValue": "", "retCode": -1, "retMsg": "xxxxx"}
'''

def issueAdoptPetInfo(data):
    EVENT_STATUS = 0
    ADOPT = 1
    userId = data.get("user_id")
    user = models.User.objects.filter(user_id = userId).first()
    if not user:
        return util.errorJsonWrapper("不存在该用户")
    activityPic = data.get("activity_picture")
    activityIntro = data.get("activity_introduction")
    activityAddr = data.get("activity_address")
    activityLongi = data.get("activity_longitude")
    activityLati = data.get("activity_latitude")
    activityPet = data.get("activity_pet_type")
    activityPrice = data.get("activity_price")
    activityStartTime = data.get("activity_start_time")
    activityEndTime = data.get("activity_end_time")
    try:
        activity = models.Activity( activity_introduction = activityIntro,
                                activity_picture = activityPic,
                                activity_price = activityPrice,
                                activity_pet_type = activityPet,
                                activity_start_time = activityStartTime,
                                activity_end_time = activityEndTime,
                                activity_status = EVENT_STATUS,
                                activity_address = activityAddr)
        activity.save()
    except Exception:
        return util.errorJsonWrapper("发布收养信息出错，activity无法写入数据库")
    try:
        participant = models.Participant(participant_user = user,
                                     participant_activity = activity,
                                     participant_user_type = ADOPT)
        participant.save()
    except Exception:
        return util.errorJsonWrapper("发布收养信息出错，participant无法写入数据库")

    return util.simpleOkJsonWrapper()

