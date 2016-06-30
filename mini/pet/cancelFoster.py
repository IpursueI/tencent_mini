#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import util
import json

def cancelFoster(data):
    userId = data.get("user_id")
    if not userId:
        return util.errorJsonWrapper("缺少user_id")

    user = models.User.objects.filter(user_id = userId).first()
    if not user:
        return util.errorJsonWrapper("该用户不存在")

    userToken = data.get("user_token")
    if not userToken:
        return util.errorJsonWrapper("token不存在")

    if not util.checkToken(userId, userToken):
        return util.errorJsonWrapper("token验证失败")

    activityId = data.get("activity_id")
    if not activityId:
        return util.errorJsonWrapper("缺少activity_id")

    activity = models.Activity.objects.filter(pk = activityId).first()
    if not activity:
        return util.errorJsonWrapper("该活动不存在")
    
    partAdopt = models.Participant.objects.filter(participant_activity = activity, participant_user_type = 1).first()
    if not partAdopt:
        return util.errorJsonWrapper("不存在该收养用户")
    

    partFoster = models.Participant.objects.filter(participant_user = user, participant_activity = activity).first()
    if not partFoster:
        return util.errorJsonWrapper("不存在该寄养用户")

    try:
        partAdopt.participant_status = 0
        partAdopt.save()
        
        partFoster.participant_status = 2
        partFoster.save()
    except:
        return util.errorJsonWrapper("写入数据库出错")

    return util.simpleOkJsonWrapper()





       
