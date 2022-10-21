from django.db import models

from django.contrib.auth.models import User

class Customer(User):
    class Meta:
        proxy = True
        
        
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)    
    sname=models.CharField(max_length=20)
    slastname=models.CharField(max_length=20)
    birthdate=models.DateField()

    

        