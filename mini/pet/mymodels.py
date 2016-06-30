from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length = 11,primary_key = True)
    user_password = models.CharField(max_length = 100)
    user_gender = models.IntegerField(default=0)
    user_age = models.IntegerField(default=0)
    user_address = models.CharField(max_length = 200, default="")
    user_avatar = models.CharField(max_length=200, default="")
    user_nickname = models.CharField(max_length = 20, default="")
    user_longitude = models.CharField(max_length = 20, default = "")
    user_latitude = models.CharField(max_length = 20, default = "")
    user_interest = models.IntegerField(default = 0)
    user_authenticated = models.BooleanField(default = False)
    user_authenticated_picture = models.CharField(max_length = 200, default="")
    user_token = models.CharField(max_length = 100, default="")
    user_token_overdue = models.CharField(max_length = 100, default="")

    def __unicode__(self):
        return self.user_id
    def printuser(self):
        print("id:%s\npassword:%s\ngender:%d\nage:%d\naddress:%s\navatar:%s\nnickname:%s\nlongtitude:%s\nlatitude:%s\ninterest:%d\nauthenticated:%d\nauthenticated_picture:%s\ntoken:%s\ntoken_overdue:\n",user_id,user_password)


class Activity(models.Model):
    activity_title = models.CharField(max_length = 30, default="")
    activity_introduction = models.CharField(max_length = 300, default="")
    activity_address = models.CharField(max_length = 200, default="")
    activity_picture = models.CharField(max_length = 200, default="")
    activity_longitude = models.CharField(max_length = 20, default = "")
    activity_latitude = models.CharField(max_length = 20, default = "")
    activity_price = models.IntegerField(default=0)
    activity_pet_type = models.IntegerField(default=0)
    activity_start_time = models.CharField(max_length = 100, default="")
    activity_end_time = models.CharField(max_length = 100, default="")
    activity_status = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.activity_introduction

class Participant(models.Model):
    participant_user = models.ForeignKey(User)
    participant_activity = models.ForeignKey(Activity)
    participant_user_type = models.IntegerField(default = 0)
    participant_status = models.IntegerField(default = 0)
