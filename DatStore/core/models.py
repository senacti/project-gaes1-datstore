from distutils.command import upload
from enum import unique
from itertools import product
from pyexpat import model
import uuid
from django.db import models
from msilib.schema import Class
from tabnanny import verbose
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.decorators import login_required
from users.models import User
from django.conf import settings

import core


#Lista estados
chstate= [('Ent', 'Entregado'),('Pen', 'Pendiente'),]

tstate= [('Act', 'Active'),('Ina', 'Inactive'),]



class TypeProduct (models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre del Producto")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Tipo de Producto'
        verbose_name_plural = 'Tipo de Productos' 
        db_table = 'TipoProducto'
        ordering = ['id']

class Supplier(models.Model):
    id = models.PositiveIntegerField(primary_key=True, verbose_name="Id del proveedor")
    name = models.TextField(max_length=20, verbose_name="Nombre del proveedor")
    phone = models.PositiveIntegerField(verbose_name="Número de telefono")
    email = models.EmailField(max_length=30, verbose_name="Email del proveedor")
    direction = models.CharField(max_length=50,verbose_name="Direccion del proveedor")
    state = models.CharField(max_length=15,verbose_name="Estado del proveedor")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name= 'Proveedor'
        verbose_name_plural = 'Preveedores'
        db_table = 'Proveedor'
        ordering = ['id']




class WayToPay(models.Model):
    name = models.TextField(max_length=15, verbose_name="Nombre de la forma de pago")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Forma de Pago'
        verbose_name_plural = 'Formas de Pago'
        db_table = 'FormaPago'
        ordering = ['id']

class Users(models.Model):
    id = models.PositiveIntegerField(primary_key=True, verbose_name="Id del Usuario")
    name = models.TextField(max_length=20, verbose_name="Primer nombre del Usuario")
    names = models.TextField(max_length=20, verbose_name="Segundo nombre del Usuario")
    lastn = models.TextField(max_length=20, verbose_name="Primer apellido del Usuario")
    lastns = models.TextField(max_length=20, verbose_name="Segundo apellido del Usuario")
    address = models.CharField(max_length=50, verbose_name="Direccion del Usuario")
    email = models.EmailField(max_length=30, verbose_name="Correo del Usuario")
    password = models.CharField(max_length=20, verbose_name="Contraseña del Usuario")
    telephone = models.PositiveIntegerField(verbose_name="Numero del Celular")
    condition = models.TextField(max_length=15, verbose_name="Estado del Usuario")


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'Usuario'
        ordering = ['id']
 
class InventoryEntry(models.Model):
    date = models.DateField(auto_now_add=True,verbose_name="Fecha entrada")
    totalpurchase = models.PositiveBigIntegerField(default=0,verbose_name="Total Compra")
    refpayment = models.CharField(max_length=10, verbose_name="Referencia de pago", null=True, blank=True)
    iduser = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Identificación del Usuario")
    idwaytopay = models.ForeignKey(WayToPay, on_delete=models.CASCADE, verbose_name="Identificación Forma Pago")   
    
    def __int__(self) -> int:
        return int(self.pk)
        
    class Meta:
        verbose_name= 'EntradaInventario'
        verbose_name_plural = 'EntradasInventario'
        db_table = 'EntradaInventario'
        ordering = ['id']

class Product(models.Model):
    id = models.PositiveIntegerField(primary_key=True, verbose_name="Id del producto")
    name = models.TextField(max_length=30, verbose_name="Nombre del producto")
    description = models.TextField(max_length=50, verbose_name="Descripción del producto", null=True, blank=True)
    costp=models.PositiveIntegerField(verbose_name="Precio producto indiv.", default=10, null=True, blank=True)
    stock = models.PositiveBigIntegerField(verbose_name="Cantidad del producto")
    state= models.CharField(max_length=20,choices=tstate, verbose_name="Estado del producto",default='Activo')
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='productos/', null=False, blank=False)
    idfksup = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Idenfiticación del Proveedor")
    idfktipp = models.ForeignKey(TypeProduct, on_delete=models.CASCADE, verbose_name="Identificación del Tipo Producto")

    #def save(self, *args, **kwargs):
        #self.slug = slugify(self.name)
        #super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
        ordering = ['id']

def set_slug(sender, instance, *args, **kwargs):
    if instance.name and not instance.slug:
        slug = slugify(instance.name)

        while Product.objects.filter(slug = slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.name, str(uuid.uuid4())[:8]))

        instance.slug = slug

pre_save.connect(set_slug, sender=Product)
 
class EntryDetail(models.Model):
    quantity = models.PositiveIntegerField(verbose_name="Cantidad de la entrada")
    dateexpiry = models.DateField(verbose_name="Fecha caducidad de los productos")
    purchaseprice = models.PositiveIntegerField(verbose_name="Precio de compra de los productos")
    groupcost = models.PositiveIntegerField(verbose_name="Coste del grupo de productos",default=0)
    idprodFK = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Identificación del producto")
    identinvFK = models.ForeignKey(InventoryEntry, on_delete=models.CASCADE, verbose_name="Identificación Entrada Inventario")
   
    def __int__(self) -> int:
        return int(self.pk)
        
    class Meta:
        verbose_name= 'DetalleEntrada'
        verbose_name_plural = 'DetallesEntrada'
        db_table = 'DetalleEntrada'
        ordering = ['id']

class Order(models.Model):
    date = models.DateField(verbose_name="Fecha del pedido")
    total= models.PositiveIntegerField(verbose_name="Total del pedido")
    chtd= [    ('Dom', 'Domicilio'),
    ('Tie', 'Tienda'),]
    typedel = models.CharField(max_length=4,choices=chtd, verbose_name="Tipo Entrega")
    #models.CharField(max_length=20,verbose_name="Tipo entrega")
    statord= models.CharField(max_length=4,choices=chstate, verbose_name="Estado Entrega")
    #models.CharField(max_length=20,verbose_name="Estado")
    refpay= models.CharField(max_length=20,null=True,verbose_name="Referencia de pago")
    idfkpayform= models.ForeignKey(WayToPay, on_delete=models.CASCADE, verbose_name="Identificación Forma Pago")
    idfkclient= models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="Identificación Cliente")
    

class DetOrder(models.Model):
    quant=models.PositiveIntegerField(verbose_name="Cantidad productos")
    costgp=models.PositiveIntegerField(verbose_name="Precio grupo producto")
    idfkprod=models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Ifentificación Producto")
    idfkord=models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Identificación Pedidos")

    def __str__(self) -> str:
        return self.idfkord

    class Meta:
        verbose_name = 'Detalle Pedido'
        verbose_name_plural = 'Detalles Pedido'
        db_table = 'Detallepedido'
        ordering = ['id']

class Inventoryoutput (models.Model):
    amount = models.PositiveIntegerField(verbose_name="Cantidad de la Salida")
    dateout = models.DateField(verbose_name="Fecha de la Salida")
    idprofk = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Identificación Producto")
    iddepefk = models.ForeignKey(Order,on_delete=models.CASCADE, verbose_name="Identificación Detalle Pedido")
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Salida del inventario'
        verbose_name_plural = 'Salidas del inventario'
        db_table = 'SalidaInventario'
        ordering = ['id']


        
        
        
