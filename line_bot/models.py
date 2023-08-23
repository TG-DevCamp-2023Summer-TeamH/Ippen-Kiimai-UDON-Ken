from django.db import models

# Create your models here.
class LINEFollower(models.Model):
    user_id = models.CharField(max_length=50)
    for shop in range(185):
        exec("udon_no_{} = models.IntegerField()".format(str(shop)))