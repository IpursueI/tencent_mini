#-*- coding:UTF-8 -*-
import json
from django.conf import settings
import time
import hashlib
import os
import models
import datetime

def checkToken(userId, token):
    user = models.User.objects.filter(user_id=userId).first()
    if not user:
        return False
        #return errorJsonWrapper("aaa")
    else:
        if str(datetime.datetime.now()) < user.user_token_overdue:
            if token == user.user_token:
                user.user_token_overdue = str(datetime.datetime.now() + datetime.timedelta(days = 3))
                user.save()
                return True
            else:
                #return errorJsonWrapper("bbb")
                return False
        else:
            return False
            #return errorJsonWrapper("ccc")

def errorJsonWrapper(errorInfo=""):
    res = dict(retCode=-1, retMsg=errorInfo, retValue="")
    return json.dumps(res)

def simpleOkJsonWrapper(okInfo=""):
    res = dict(retCode=0, retMsg=okInfo, retValue="")
    return json.dumps(res)


def savePicture(files, name):
    if files:  #如果该request携带文件数据
        try:
            picture = files[name] #图像的key
            pictureSavedName = time.strftime("%Y%m%d%H%M%S")+picture.name
            nameList = pictureSavedName.split('.')
            pictureSavedName = hashlib.md5(nameList[0]).hexdigest()+"."+nameList[1]
            filePath = os.path.join(settings.MEDIA_ROOT, pictureSavedName)
       
            with open(filePath, 'wb+') as destination:
                for chunk in picture.chunks():
                    destination.write(chunk)
        except:
            return ""

        pictureUrl = "media/"+pictureSavedName
        return pictureUrl
    else:
        return ""



def intelligentSort(userId, sortType):
    user = models.User.objects.filter(user_id = userId)
    if sortType == 1:
        return models.Participant.objects.filter(participant_user_type=1, participant_user__user_gender=2-user[0].user_gender)
    else:
        return models.Participant.objects.filter(participant_user_type=1)
