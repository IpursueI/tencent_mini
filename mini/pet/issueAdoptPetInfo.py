#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import datetime
import util
import json
import hashlib
import time
import os
from django.conf import settings

'''
发布收养信息：by stanwu, 2016/06/25  --> modify by perryhuang, 2016/06/27 , add save activity_picture function
post参数名：method
post参数内容：
	{"name":"issueAdoptPetInfo","args":{"user_id":"xxx","activity_introduction":"xxx",
 	"activity_address":"xxx","activity_longitude":"xxx","activity_latitude":"xxx",
	"activity_pet_type":xxx,"activity_price":xxx,
	"activity_start_time":"xxx", "activity_end_time":"xxx"}}

服务器返回值(json格式):
    注册成功：
    {"retValue": "", "retCode": 0, "retMsg": ""}
    注册失败：
    {"retValue": "", "retCode": -1, "retMsg": "xxxxx"}
'''

def issueAdoptPetInfo(data,files):
    EVENT_STATUS = 1
    ADOPT = 1

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

    user = models.User.objects.filter(user_id = userId).first()
    if not user:
        return util.errorJsonWrapper("不存在该用户")

    if not user.user_authenticated:
        return util.errorJsonWrapper("failed")
    
    activityIntro = data.get("activity_introduction")
    activityAddr = data.get("activity_address")
    activityLongi = data.get("activity_longitude")
    activityLati = data.get("activity_latitude")
    activityPet = data.get("activity_pet_type")
    activityPrice = data.get("activity_price")
    activityStartTime = data.get("activity_start_time")
    activityEndTime = data.get("activity_end_time")
    activityStartTime = time.strftime("%Y-%m-%d",(time.strptime(activityStartTime,"%Y-%m-%d")))
    activityEndTime = time.strftime("%Y-%m-%d",(time.strptime(activityEndTime,"%Y-%m-%d")))

    resDict = {}
    resDict['activity_introduction'] = activityIntro
    resDict['activity_address'] = activityAddr
    resDict['activity_longitude'] = activityLongi
    resDict['activity_latitude'] = activityLati
    resDict['activity_pet_type'] = activityPet
    resDict['activity_price'] = activityPrice
    resDict['activity_start_time'] = activityStartTime
    resDict['activity_end_time'] = activityEndTime
    resDict["user_id"] = user.user_id
    resDict["user_nickname"] = user.user_nickname
    resDict["user_avatar"] = user.user_avatar
    resDict["user_address"] = user.user_address
    resDict["user_age"] = user.user_age
    resDict["user_interest"] = user.user_interest
    resDict["user_gender"] = user.user_gender
    resDict["user_authenticated"] = user.user_authenticated


    picName = util.savePicture(files,"activity_picture",20*1024*1024)
    if picName == -1:
        return util.errorJsonWrapper("failed")
    activityPic = picName 

    try:

        activity = models.Activity(activity_introduction = activityIntro,
                                activity_picture = activityPic,
                                activity_price = activityPrice,
                                activity_pet_type = activityPet,
                                activity_start_time = activityStartTime,
                                activity_end_time = activityEndTime,
                                activity_status = EVENT_STATUS,
                                activity_latitude = activityLati,
                                activity_longitude = activityLongi,
                                activity_address = activityAddr)
        activity.save()
    except Exception:
        return util.errorJsonWrapper("发布收养信息出错，activity无法写入数据库")

    resDict["activity_id"] = activity.pk
    resDict["activity_picture"] = picName

    try:
        participant = models.Participant(participant_user = user,
                                     participant_activity = activity,
                                     participant_user_type = ADOPT)
        participant.save()
    except Exception:
        return util.errorJsonWrapper("发布收养信息出错，participant无法写入数据库")
    
    #userDict = {"user_id" : userId} 
    res = dict(retCode = 0, retMsg = "", retValue = resDict)
    return json.dumps(res)
