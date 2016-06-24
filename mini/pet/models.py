from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length = 11,primary_key = True)
    user_password = models.CharField(max_length = 100)
    user_gender = models.BooleanField(default=True)
    user_age = models.IntegerField()
    user_address = models.CharField(max_length = 200)
    user_avatar = models.ImageField()
    user_nickname = models.CharField(max_length = 20)
    user_longitude = models.DecimalField(max_digits=6, decimal_places=3)
    user_latitude = models.DecimalField(max_digits=6, decimal_places=3)
    user_interest = models.IntegerField()
    user_authenticated = models.BooleanField()
    user_authenticated_picture = models.ImageField()


class Activity(models.Model):
    activity_title = models.CharField(max_length = 30)
    activity_introduction = models.CharField(max_length = 300)
    activity_picture = models.ImageField()
    activity_start_time = models.TimeField()
    activity_end_time = models.TimeField()
    activity_status = models.IntegerField(default = 0)

class Participant(models.Model):
    participant_user_id = models.ForeignKey(User)
    participant_activity_id = models.ForeignKey(Activity)
    participant_user_type = models.BooleanField()
