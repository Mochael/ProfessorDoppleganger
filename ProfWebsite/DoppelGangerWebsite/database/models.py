from django.db import models

# Create your models here.
class Professors(models.Model):
    profName = models.CharField(max_length=50)
    profPic = models.CharField(default="", max_length=400)

class User(models.Model):
    userPic = models.CharField(default="", max_length=400)