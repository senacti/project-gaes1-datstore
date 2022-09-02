from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('Compras/', views.compras, name='Compras'),
    path('DetallePed/', views.detallePed, name='DetallePedidoInventario'),
    path('Domicilio/', views.domicilio, name='Domicilio'),
    path('Estado/', views.estado, name='Estado'),
    path('FormaPago/', views.formaPago, name='FormaPago'),
    path('Graficos/', views.graficos, name='Graficos'),
    path('Inventario/', views.inventario, name='Inventario'),
    path('Pedido/', views.pedido, name='Pedido'),
    path('Producto/', views.producto, name='Producto'),
    path('Proveedor/', views.proveedor, name='Proveedor'),
    path('Rol/', views.rol, name='Rol'),
    path('TipoProducto/', views.tipoprod, name='TipoProducto'),
    path('Usuario/', views.usuario, name='Usuario'),
    path('Ventas/', views.ventas, name='Ventas')
]
