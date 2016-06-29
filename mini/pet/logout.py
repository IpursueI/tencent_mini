#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import util
import json
import hashlib
import datetime

def logout(data):

    userID = data.get("user_id")
    user = models.User.objects.filter(user_id = userID).first()

    if not user:
        return util.errorJsonWrapper("不存在该用户名")
    else:
        user.user_token_overdue = str(datetime.datetime.now())
        user.save()
        return util.simpleOkJsonWrapper()
