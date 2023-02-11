from django.db import models

from django.contrib.auth.models import AbstractUser
from orders.common import OrderStatus


froles= [('Adm', 'Admin'),('Emp', 'Employee'),('Cli', 'Client'),]



class User(AbstractUser):

    email=models.EmailField(unique=True,verbose_name="Email")
    phone = models.PositiveIntegerField(default=0,verbose_name="Teléfono")
    birthdate=models.DateField(null=True, blank=True,verbose_name="Fecha de nacimiento")
    

    def __str__(self):
        return str(self.username)

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
  
        


    

        