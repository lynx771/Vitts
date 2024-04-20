from django.db import models

class regtable(models.Model):
    name=models.CharField(max_length=150) 
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150) 
    phone=models.CharField(max_length=150) 


class uploadtable(models.Model):
    images=models.CharField(max_length=150) 
    result=models.CharField(max_length=150) 
    user_id=models.CharField(max_length=150) 
