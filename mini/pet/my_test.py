#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import util
import json
import hashlib

def cleanUser():
    users = models.User.objects.all()
    for item in users:
        item.delete()

    print "User 表数据已经清空"


def cleanActivity():
    activities = models.Activity.objects.all()
    for item in activities:
        item.delete()

    print "Activity 表数据已经清空"


def cleanParticipant():
    participant = models.Participant.objects.all()
    for item in participant:
        item.delete()

    print "Participant 表数据已经清空"
    
cleanUser()
cleanActivity()
cleanParticipant()
