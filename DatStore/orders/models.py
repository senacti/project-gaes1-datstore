import uuid
import decimal

from django.db import models

from users.models import User
from carts.models import Cart
from promo_codes.models import PromoCode

from shipping_addresses.models import ShippingAddress

from .common import OrderStatus
from .common import choices

from django.db.models.signals import pre_save
from django.conf import settings



class Order(models.Model):
    order_id=models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name="Codigo del Pedido")
    user= models.ForeignKey(User, on_delete=models.CASCADE , verbose_name="Usuario")
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="Carrito" )
    status=models.CharField(max_length=50, choices=choices, default=OrderStatus.CREATED)
    shipping_total=models.DecimalField(default=1000, max_digits=8, decimal_places=2, verbose_name="Total del envio")
    total=models.DecimalField(default=0,max_digits=8, decimal_places=2, verbose_name="Total")
    created_at= models.DateField(auto_now_add=True, verbose_name="Creado el:")
    shipping_address=models.ForeignKey(ShippingAddress, 
                                      null=True, blank=True, 
                                      on_delete=models.CASCADE , verbose_name="Direccion del pedido")
    promo_code = models.ForeignKey(PromoCode, null=True, blank=True,
                                        on_delete = models.CASCADE, verbose_name="Codigo de promación")
    address= models.TextField(max_length=130,verbose_name="Direccion", null=True, blank=True)

    def __str__(self):
        return self.order_id

    
    def apply_promo_code(self, promo_code):
        if self.promo_code is None:
            self.promo_code = promo_code
            self.save()

            self.update_total()
            promo_code.use()

    def get_or_set_shipping_address(self):
        if self.shipping_address:
            return self.shipping_address
        
        shipping_address = self.user.shipping_address
        if shipping_address:
            self.update_shipping_address(shipping_address)
        

        return shipping_address

    def update_shipping_address(self, shipping_address):
        self.shipping_address=shipping_address
        self.save()

    def complete(self):
        self.status=OrderStatus.COMPLETED
        self.save()

    def cancel(self):
        self.status=OrderStatus.CANCELED
        self.save
 

    def update_total(self):
        self.total = self.get_total()
        self.save()

    def get_discount(self):
        if self.promo_code:
            return self.promo_code.discount
        return 0

    def get_total(self):
        return self.cart.total + self.shipping_total - decimal.Decimal(self.get_discount())

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']


def set_order_id(sender, instance, *args,**kwargs):
    if not instance.order_id:
        instance.order_id = str (uuid.uuid4())

def set_total(sender, instance, *args, **kwargs):
    instance.total=instance.get_total()


class Delivery(models.Model):
    direction = models.CharField(max_length=150, verbose_name="Direccion a dónde irá el domicilio")
    price = models.PositiveIntegerField(verbose_name="Precio del domicilio")
    idpedidoFK = models.OneToOneField(Order, on_delete=models.CASCADE, verbose_name="Identificación Pedido")
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Identificación del Usuario")
    deliver= models.CharField(max_length=60, verbose_name="Nombre del repartidor",default="Repartidor")

    def str(self) -> str:
        return self.direction

    class Meta:
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domicilios'
        db_table = 'Domicilios'
        ordering = ['id']




pre_save.connect(set_order_id, sender=Order)
pre_save.connect(set_total, sender=Order)