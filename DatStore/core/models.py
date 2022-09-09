from django.db import models
from msilib.schema import Class
from tabnanny import verbose
from unittest.util import _MAX_LENGTH


#Lista estados
chstate= [('Ent', 'Entregado'),('Pen', 'Pendiente'),]



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
    id = models.IntegerField(primary_key=True, verbose_name="Id del proveedor")
    name = models.CharField(max_length=20, verbose_name="Nombre del proveedor")
    phone = models.IntegerField(verbose_name="Número de telefono")
    email = models.CharField(max_length=30, verbose_name="Email del proveedor")
    direction = models.CharField(max_length=50,verbose_name="Direccion del proveedor")
    state = models.CharField(max_length=15,verbose_name="Estado del proveedor")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name= 'Proveedor'
        verbose_name_plural = 'Preveedores'
        db_table = 'Proveedor'
        ordering = ['id']

class Rol (models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre del Rol")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        db_table = 'Rol'
        ordering = ['id']

class Permission(models.Model):
    name = models.CharField(max_length=20, verbose_name="Nombre del permiso")
    idprodFK = models.ManyToManyField(Rol)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Permiso'
        verbose_name_plural = 'Categorias'
        db_table = 'Permiso'
        ordering = ['id']


class WayToPay(models.Model):
    name = models.CharField(max_length=15, verbose_name="Nombre de la forma de pago")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Forma de Pago'
        verbose_name_plural = 'Formas de Pago'
        db_table = 'FormaPago'
        ordering = ['id']

class User(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name="Id del Usuario")
    name = models.CharField(max_length=20, verbose_name="Primer nombre del Usuario")
    names = models.CharField(max_length=20, verbose_name="Segundo nombre del Usuario")
    lastn = models.CharField(max_length=20, verbose_name="Primer apellido del Usuario")
    lastns = models.CharField(max_length=20, verbose_name="Segundo apellido del Usuario")
    address = models.CharField(max_length=50, verbose_name="Direccion del Usuario")
    email = models.CharField(max_length=30, verbose_name="Correo del Usuario")
    password = models.CharField(max_length=20, verbose_name="Contraseña del Usuario")
    telephone = models.BigIntegerField(verbose_name="Numero del Celular")
    condition = models.CharField(max_length=15, verbose_name="Estado del Usuario")
    idrolfk = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'Usuario'
        ordering = ['id']
 
class InventoryEntry(models.Model):
    date = models.DateField(verbose_name="Fecha entrada")
    totalpurchase = models.IntegerField(verbose_name="Total Compra")
    refpayment = models.CharField(max_length=10, verbose_name="Referencia de pago")
    iduser = models.ForeignKey(User, on_delete=models.CASCADE)
    idwaytopay = models.ForeignKey(WayToPay, on_delete=models.CASCADE)   
    
    def __str__(self) -> str:
        return self.iduser
        
    class Meta:
        verbose_name= 'EntradaInventario'
        verbose_name_plural = 'EntradasInventario'
        db_table = 'EntradaInventario'
        ordering = ['id']

class Product(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name="Id del producto")
    name = models.CharField(max_length=20, verbose_name="Nombre del producto")
    stock = models.IntegerField(verbose_name="Descripcion del producto")
    state = models.CharField(max_length=20, verbose_name="Estado del producto")
    idfksup = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    idfktipp = models.ForeignKey(TypeProduct, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
        ordering = ['id']
 
class EntryDetail(models.Model):
    quantity = models.IntegerField(verbose_name="Cantidad de la entradad")
    dateexpiry = models.DateField(verbose_name="Fecha caducidad de los productos")
    purchaseprice = models.BigIntegerField(verbose_name="Precio de compra de los productos")
    groupcost = models.BigIntegerField(verbose_name="Coste del grupo de productos")
    idprodFK = models.ForeignKey(Product, on_delete=models.CASCADE)
    identinvFK = models.ForeignKey(InventoryEntry, on_delete=models.CASCADE)
   
    def __str__(self) -> str:
        return self.idprodFK
        
    class Meta:
        verbose_name= 'DetalleEntrada'
        verbose_name_plural = 'DetallesEntrada'
        db_table = 'DetalleEntrada'
        ordering = ['id']

class Order(models.Model):
    date = models.DateField(verbose_name="Fecha del pedido")
    total= models.BigIntegerField(verbose_name="Total del pedido")
    chtd= [    ('Dom', 'Domicilio'),
    ('Tie', 'Tienda'),]
    typedel = models.CharField(max_length=4,choices=chtd, verbose_name="Tipo Entrega")
    #models.CharField(max_length=20,verbose_name="Tipo entrega")
    statord= models.CharField(max_length=4,choices=chstate, verbose_name="Estado Entrega")
    #models.CharField(max_length=20,verbose_name="Estado")
    refpay= models.CharField(max_length=20,null=True,verbose_name="Referencia de pago")
    idfkpayform= models.ForeignKey(WayToPay, on_delete=models.CASCADE)
    idfkclient= models.ForeignKey(User, on_delete=models.CASCADE)

class DetOrder(models.Model):
    quant=models.IntegerField(verbose_name="Cantidad productos")
    costp=models.BigIntegerField(verbose_name="Precio producto indiv.")
    costgp=models.BigIntegerField(verbose_name="Precio grupo producto")
    idfkprod=models.ForeignKey(Product, on_delete=models.CASCADE)
    idfkord=models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.idfkord

    class Meta:
        verbose_name = 'Detalle Pedido'
        verbose_name_plural = 'Detalles Pedido'
        db_table = 'Detallepedido'
        ordering = ['id']



class inventoryoutput (models.Model):
    amount = models.IntegerField(verbose_name="Cantidad de la Salida")
    dateout = models.DateField(verbose_name="Fecha de la Salida")
    idprofk = models.ForeignKey(Product, on_delete=models.CASCADE)
    iddepefk = models.ForeignKey(Order,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Salida del inventario'
        verbose_name_plural = 'Salidas del inventario'
        db_table = 'SalidaInventario'
        ordering = ['id']


class delivery(models.Model):
    direction = models.CharField(max_length=60, verbose_name="Direccion a dónde irá el domicilio")
    price = models.BigIntegerField(verbose_name="Precio del domicilio")
    idPedidoFK = models.ForeignKey(Order, on_delete=models.CASCADE)
    idEmpleadoFK = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.direction

    class Meta:
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domicilios'
        db_table = 'Domicilios'
        ordering = ['id']
        
        
        
    
    
