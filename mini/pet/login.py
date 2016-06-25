#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import util
import json
import hashlib

def login(data):
    userID = data.get("user_id")
    password = data.get("user_password")
    user = models.User.objects.filter(user_id = userID).first()
    if not user:
        return util.errorJsonWrapper("不存在该用户名")
    else:
        if not password:
            return util.errorJsonWrapper("请输入密码")
        elif user.user_password != hashlib.md5(password).hexdigest():
            return util.errorJsonWrapper("密码错误")
        else:
            return util.simpleOkJsonWrapper()
            
            
            
        
        
        
        
