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
    else:
        if str(datetime.datetime.now()) < user.user_token_overdue:
            if token == user.user_token:
                user.user_token_overdue = str(datetime.datetime.now() + datetime.timedelta(days = 3))
                user.save()
                return True
            else:
                return False
        else:
            return False

def errorJsonWrapper(errorInfo=""):
    res = dict(retCode=-1, retMsg=errorInfo, retValue="")
    return json.dumps(res)

def simpleOkJsonWrapper(okInfo=""):
    res = dict(retCode=0, retMsg=okInfo, retValue="")
    return json.dumps(res)


def savePicture(files, name, picSize):
    if files:  #如果该request携带文件数据
        try:
            picture = files[name] #图像的key
            if not checkPicture(picture, picSize):
                return -1 
            pictureSavedName = time.strftime("%Y%m%d%H%M%S")+picture.name
            nameList = pictureSavedName.split('.')
            pictureSavedName = hashlib.md5(nameList[0]).hexdigest()+"."+nameList[1]
            filePath = os.path.join(settings.MEDIA_ROOT, pictureSavedName)
       
            with open(filePath, 'wb+') as destination:
                for chunk in picture.chunks():
                    destination.write(chunk)
        except:
            return -1

        pictureUrl = "media/"+pictureSavedName
        return pictureUrl
    else:
        return ""

def checkPicture(picture, picSize):
    #return True
    name = picture.name
    form = name.split('.')[1].lower()
    if form not in ['jpg','png','jpeg','gif']:
        return False
    if picture._size > picSize:
        return False
    return True

def intelligentSort(userId, sortType):
    GENDER = 1
    INTEREST = 2
    user = models.User.objects.filter(user_id = userId).first()
    if not user:
        return []

    if sortType == GENDER:
        return models.Participant.objects.filter(participant_user_type=1, participant_user__user_gender=3-user.user_gender)
    elif sortType == INTEREST:
        tag = user.user_interest
        partList = models.Participant.objects.filter(participant_user_type=1)
        tagDiff = 0
        recommendDict = {}
        for participant in partList:
            recommendDict[participant] = str(bin(tag^participant.participant_user.user_interest)).count("1")
        sortedList = sorted(recommendDict.items(), lambda x, y:cmp(x[1],y[1]))
                                                                                                                        
        return [item[0] for item in sortedList]
                                                                                                                                
    else:
        return models.Participant.objects.filter(participant_user_type=1)
