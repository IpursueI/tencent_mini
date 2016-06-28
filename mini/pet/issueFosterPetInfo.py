#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import util
import json

def issueFosterPetInfo(data):
    try:
        userId = data["user_id"]
    except KeyError:
        return util.errorJsonWrapper("寄养消息没有user_id字段")

    try:
        activityId = data["activity_id"]
    except KeyError:
        return util.errorJsonWrapper("寄养消息没有activity_id字段")
    
    checkUserId = models.User.objects.filter(user_id=userId)
    if len(checkUserId) == 0:
        return util.errorJsonWrapper("不存在该userId用户")

    checkActivityId = models.Activity.objects.filter(pk=activityId)
    if len(checkActivityId) == 0:
        return util.errorJsonWrapper("不存在该activity_id活动")


    try:
        tmpParticipant = models.Participant(participant_user = checkUserId[0], participant_activity = checkActivityId[0], participant_user_type=2)
        tmpParticipant.save()
        return util.simpleOkJsonWrapper()
    except Exception:
        return util.errorJsonWrapper("Participant 数据写入数据库出错")
