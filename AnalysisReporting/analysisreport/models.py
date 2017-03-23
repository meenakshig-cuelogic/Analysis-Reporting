
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

 
class emailverify(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    hashkey = models.CharField(max_length=50)
    
    

