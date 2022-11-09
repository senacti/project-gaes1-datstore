from django.db import models

from django.contrib.auth.models import AbstractUser
from orders.common import OrderStatus


class User(AbstractUser):

    @property
    def shipping_address(self):
        return self.shippingaddress_set.filter(default=True).first()
        
    def  get_full_name(self):
        return '{} {}'.format(self.first_name,self.last_name)

    def orders_completed(self):
        return self.order_set.filter(status=OrderStatus.COMPLETED).order_by('-id')

    def has_shipping_addresses(self):
        return self.shippingaddres_set.exists()

    @property
    def addresses(self):
        return self.shippingaddress_set.all()

class Customer(User):
    class Meta:
        proxy = True
  
        
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)    
    sname=models.CharField(max_length=20)
    slastname=models.CharField(max_length=20)
    birthdate=models.DateField()


    

        