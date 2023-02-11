from django.db import models

from users.models import User

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    line1 = models.CharField(max_length=200)
    reference= models.CharField(max_length=300)
    postal_code= models.CharField(max_length=10)
    default = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.postal_code

    @property
    def direct(self):
         return "%s - %s - %s" % ( self.line1, self.reference,self.postal_code )

    def has_orders(self):
        return self.order_set.count()>=1

    def update_default(self, default=False):
        self.default= default
        self.save()


