#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import util
import json

def issueFosterPetInfo(data):
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
        activityId = data["activity_id"]
    except KeyError:
        return util.errorJsonWrapper("寄养消息没有activity_id字段")
     
    checkUserId = models.User.objects.filter(user_id=userId)
    if len(checkUserId) == 0:
        return util.errorJsonWrapper("不存在该userId用户")

    checkActivityId = models.Activity.objects.filter(pk=activityId)
    if len(checkActivityId) == 0:
        return util.errorJsonWrapper("不存在该activity_id活动")
    
    #判断该活动是否已经被别人寄养
    isParAdopted = models.Participant.objects.filter(participant_activity = checkActivityId[0], participant_user_type = 1,
            participant_status = 1)

    if isParAdopted:
        return util.errorJsonWrapper("该活动已经被别人寄养")

    #判断是否已经有取消状态的订单
    parti = models.Participant.objects.filter(participant_user = checkUserId[0], participant_activity = checkActivityId[0], 
            participant_user_type = 2, participant_status = 2)
    try:
        if parti:
            parti.participant_status = 1
            parti.save()
        else:
            tmpParticipant = models.Participant(participant_user = checkUserId[0], participant_activity = checkActivityId[0], 
                    participant_user_type=2, participant_status = 1)
            tmpParticipant.save()


        adoptParticipant = models.Participant.objects.filter(participant_activity = checkActivityId[0], participant_user_type=1)
        for parti in adoptParticipant:
            parti.participant_status = 1
            parti.save()
    
        return util.simpleOkJsonWrapper()
    except Exception:
        return util.errorJsonWrapper("Participant 数据写入数据库出错")
