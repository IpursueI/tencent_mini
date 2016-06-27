#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import util
import json
import hashlib
import datetime
import time

'''
登陆功能：by stanwu, 2016/06/25

post参数名：method
post参数内容：{"name":"login", "args":{"user_id":"15666666666", "user_password":"123"}}

服务器返回值(json格式):
    注册成功：
    {"retValue": "", "retCode": 0, "retMsg": ""}
    注册失败：
    {"retValue": "", "retCode": -1, "retMsg": "xxxxx"}

token用作身份验证,token验证错误，则无法访问

chayfan修改: 加入token验证，若token过期，进行密码登录，同时更新token值与tokenoverdue值

'''
def login(data):
    userID = data.get("user_id")
    token = data.get("user_token")
    password = data.get("user_password")
    user = models.User.objects.filter(user_id = userID).first()

    if not user:
        return util.errorJsonWrapper("不存在该用户名")
    else:
        if token:
            if str(datetime.datetime.now()) < user.user_token_overdue:
                if token == user.user_token:
                    return util.simpleOkJsonWrapper()
                else:
                    return util.errorJsonWrapper("token错误")
            else:
                return util.errorJsonWrapper("token已过期")


        if password:
            if user.user_password != hashlib.md5(password).hexdigest():
                return util.errorJsonWrapper("密码错误")
            else:
                token = hashlib.md5(userID + password + str(datetime.datetime.now())).hexdigest()
                user.user_token = token
                user.user_token_overdue = str(datetime.datetime.now() + datetime.timedelta(seconds = 30))
                user.save()
                tokenDict = {"user_token" : token}
                #retList = []
                #retList.append(tokenDict)
                res = dict(retCode=0, retMsg="", retValue = tokenDict)
                return json.dumps(res)
            
            
            
        
        
        
        
