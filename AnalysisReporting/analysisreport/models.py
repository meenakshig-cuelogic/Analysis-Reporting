

from django.db import models

# Create your models here.

 
class Appusers(models.Model):
     username = models.CharField(max_length=25)
     email=models.CharField(max_length=50)
     password=models.CharField(max_length=20)
