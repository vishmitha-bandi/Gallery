from django.db import models
#from django.contrib.auth.models import AbstractUser

class photos(models.Model):
    name=models.CharField( max_length=50)
    image =models.ImageField(upload_to='pics', height_field=None, width_field=None, max_length=None)
    