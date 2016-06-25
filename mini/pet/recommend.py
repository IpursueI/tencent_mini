#-*- coding:UTF-8 -*-
from django.http import HttpResponse
import models
import util
import json
import hashlib

def recommend(data):
    userID = data["user_id"]
    user = models.User.objects.filter(user_id = userID)[0]
    user.user_interest = data["user_interest"]
    user.save()

