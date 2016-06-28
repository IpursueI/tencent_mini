#-*- coding:UTF-8 -*-
import os
import sys
from django.http import HttpResponse
import models
import util
import json
from django.conf import settings

def authenticateUser(data, files):
    try:
        userId = data["user_id"]
    except KeyError:
        return util.errorJsonWrapper("注册数据没有user_id字段")

    user = models.User.objects.get(user_id=userId)

    if user:
        try:
            user.user_authenticated_picture = util.savePicture(files,"user_authenticated_picture")
            user.user_authenticated = True
            user.save()

        except Exception:
            return util.errorJsonWrapper("用户认证信息存入数据库出错")

        return util.simpleOkJsonWrapper("用户认证成功")
    else:
        return util.errorJsonWrapper("该用户不存在")


#def saveUserAvatar(files):
#    if files:  #如果该request携带文件数据
#        try:
#            avatar = files["user_avatar"] #图像的key
#            avatarSavedName = time.strftime("%Y%m%d%H%M%S")+avatar.name
#            nameList = avatarSavedName.split('.')
#            avatarSavedName = hashlib.md5(nameList[0]).hexdigest()+"."+nameList[1]
#            filePath = os.path.join(settings.MEDIA_ROOT,avatarSavedName)
#       
#            with open(filePath, 'wb+') as destination:
#                for chunk in avatar.chunks():
#                    destination.write(chunk)
#        except:
#            return ""
#
#        avatarUrl = "media/"+avatarSavedName
#        return avatarUrl
#    else:
#        return ""
