
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

# Create your models here.

 
class emailverify(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    hashkey = models.CharField(max_length=50)
    Reg_time= models.DateTimeField(default=datetime.now, blank=True)

    def is_registered_recently(self):
         cur_time = timezone.now()
         return cur_time - datetime.timedelta(days=1) <= self.pub_date <= cur_time
    
class Document(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	docfile = models.FileField(default=None,upload_to='media/')
	file_data = models.TextField(default=None)