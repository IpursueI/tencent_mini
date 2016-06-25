#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import util
import json
import hashlib

'''
登陆功能：by stanwu, 2016/06/25

post参数名：method
post参数内容：{"name":"login", "args":{"user_id":"15666666666", "user_password":"123"}}

服务器返回值(json格式):
    注册成功：
    {"retValue": "", "retCode": 0, "retMsg": ""}
    注册失败：
    {"retValue": "", "retCode": -1, "retMsg": "xxxxx"}
'''
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
            
            
            
        
        
        
        
