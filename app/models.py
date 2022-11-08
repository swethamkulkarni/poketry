from django.db import models

# Create your models here.
class Buyer(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField(default='xyz@gmail.com',max_length=254,unique=True)
    password=models.CharField(max_length=20)
    

