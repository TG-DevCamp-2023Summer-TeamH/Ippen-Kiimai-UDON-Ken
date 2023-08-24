from django.db import models

# Create your models here.
class LINEFollower(models.Model):
    user_id = models.CharField(max_length=50)
    nickname = models.CharField(max_length=100)
    mode = models.CharField(max_length=15)
    stamp = models.CharField(max_length=200)