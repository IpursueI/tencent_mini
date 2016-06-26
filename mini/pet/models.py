from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length = 11,primary_key = True)
    user_password = models.CharField(max_length = 100)
    user_gender = models.IntegerField(default=0)
    user_age = models.IntegerField(default=0)
    user_address = models.CharField(max_length = 200, default="")
    user_avatar = models.BinaryField(default=b"0")
    user_nickname = models.CharField(max_length = 20, default="")
    user_longitude = models.DecimalField(max_digits=6, decimal_places=3, default=0.0)
    user_latitude = models.DecimalField(max_digits=6, decimal_places=3, default=0.0)
    user_interest = models.IntegerField(default = 0)
    user_authenticated = models.BooleanField(default = False)
    user_authenticated_picture = models.ImageField(default="")

    def __unicode__(self):
        return self.user_id


class Activity(models.Model):
    activity_title = models.CharField(max_length = 30, default="")
    activity_introduction = models.CharField(max_length = 300, default="")
    activity_address = models.CharField(max_length = 200, default="")
    activity_picture = models.BinaryField(default=b"0")
    activity_price = models.IntegerField(default=0)
    activity_pet_type = models.IntegerField(default=0)
    activity_start_time = models.DateField(null = True)
    activity_end_time = models.DateField(null = True)
    activity_status = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.activity_introduction

class Participant(models.Model):
    participant_user = models.ForeignKey(User)
    participant_activity = models.ForeignKey(Activity)
    participant_user_type = models.IntegerField(default = 0)
