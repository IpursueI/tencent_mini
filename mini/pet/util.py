#-*- coding:UTF-8 -*-
import json
from django.conf import settings
import time
import hashlib
import os

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
