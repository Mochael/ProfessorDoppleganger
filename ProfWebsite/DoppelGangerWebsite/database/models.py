from django.db import models
from django import forms

# Create your models here.
class Professors(models.Model):
    profName = models.CharField(max_length=50)
    profPic = models.CharField(default="", max_length=400)

class User(models.Model):
    image = models.ImageField(upload_to='PostStorage')
    class Meta:
      db_table = "profile"






#class ImageUploadForm(forms.Form):
#    image = forms.ImageField()

#class ExampleModel(models.Model):
#    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')