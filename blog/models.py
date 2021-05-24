from django.contrib.auth.forms import UsernameField
from django.db import models

# Create your models here.

class Post(models.Model):
    title= models.CharField(max_length=200)
    desc= models.TextField()
    photo = models.ImageField(upload_to='myimage', width_field=None)
    
    
class Report(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    message=models.TextField()

