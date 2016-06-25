#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import util
import json
import hashlib

def login(data):
    userID = data["user_id"]
    user = models.User.objects.filter(user_id = userID)
    if not user:
        return util.errorJsonWrapper("不存在该用户名")
    else:
        if user[0].user_password != hashlib.md5(data["user_password"]).hexdigest():
            return util.errorJsonWrapper("密码错误")
        else:
            return util.simpleOkJsonWrapper()
            
            
            
        
        
        
        
