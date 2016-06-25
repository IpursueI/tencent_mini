#-*- coding:UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import util
import json
import register
import login

def index(request):
    if request.method == "POST":
        return functionChoice(request.POST.get("method","postFormError"))
    else:
        return HttpResponse(util.errorJsonWrapper("只支持POST方法"))


def functionChoice(methodData):
    if methodData == "postFormError":
        return HttpResponse(util.errorJsonWrapper("post数据没有method字段"))
    else:
        try:
            data = json.loads(methodData)
        except ValueError:
            return HttpResponse(util.errorJsonWrapper("json数据格式错误，无法解析"))
        try:
            funcName = data["name"]
        except KeyError:
            return HttpResponse(util.errorJsonWrapper("json数据格式中没有name字段"))
        try:
            funcArgs = data["args"]
        except KeyError:
            return HttpResponse(util.errorJsonWrapper("json数据格式中没有args字段"))

        if funcName == "register":
            return register.register(funcArgs)
        elif funcName == "login":
            return login.login(funcArgs)
        else:
            return HttpResponse(util.errorJsonWrapper(funcName+u":暂不支持该函数"))




