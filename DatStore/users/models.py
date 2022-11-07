from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    @property
    def shipping_address(self):
        return self.shippingaddress_set.filter(default=True).first()
    def  get_full_name(self):
        return '{} {}'.format(self.first_name,self.last_name)


class Customer(User):
    class Meta:
        proxy = True
  
        
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)    
    phone = models.PositiveIntegerField()
    sname=models.CharField(max_length=20)
    slastname=models.CharField(max_length=20)
    birthdate=models.DateField()


    

        