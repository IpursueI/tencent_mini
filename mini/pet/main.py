#-*- coding:UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import util
import json
import register
import completeUserInfo
import login
import issueAdoptPetInfo
import issueFosterPetInfo
import getInfoList
import getAdoptDetailList


def index(request):
    if request.method == "POST":
        #return functionChoice(request.POST.get("method","postFormError"))
        return functionChoice(request.POST, request.FILES)
    else:
        return HttpResponse(util.errorJsonWrapper("只支持POST方法"))

def functionChoice(post, files):
    methodData = post.get("method", "postFormError")

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
            return HttpResponse(register.register(funcArgs))
        elif funcName == "completeUserInfo":
            return HttpResponse(completeUserInfo.completeUserInfo(funcArgs,files))
        if funcName == "login":
            return HttpResponse(login.login(funcArgs))
        if funcName == "issueAdoptPetInfo":
            return HttpResponse(issueAdoptPetInfo.issueAdoptPetInfo(funcArgs,files))
        elif funcName == "issueFosterPetInfo":
            return HttpResponse(issueFosterPetInfo.issueFosterPetInfo(funcArgs))
        elif funcName == "getInfoList":
            return HttpResponse(getInfoList.getInfoList(funcArgs))
        elif funcName == "getAdoptDetailList":
            return HttpResponse(getAdoptDetailList.getAdoptDetailList(funcArgs))
        else:
            return HttpResponse(util.errorJsonWrapper(funcName+u":暂不支持该函数"))
