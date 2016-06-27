#-*- coding:UTF-8 -*-
import json

def errorJsonWrapper(errorInfo):
    res = dict(retCode=-1, retMsg=errorInfo, retValue="")
    return json.dumps(res)

def simpleOkJsonWrapper():
    res = dict(retCode=0, retMsg="", retValue="")
    return json.dumps(res)


