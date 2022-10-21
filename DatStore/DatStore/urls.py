from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('Compras/', views.compras, name='compra'),
    path('DetallePedido/', views.detallePed, name='detallepedido'),
    path('Domicilio/', views.domicilio, name='domicilio'),
    path('Estado/', views.estado, name='estado'),
    path('FormaPago/', views.formaPago, name='formapago'),
    path('reportes/', views.graficos, name='reportes'),
    path('Inventario/', views.inventario, name='inventario'),
    path('Pedido/', views.pedido, name='pedido'),
    path('Producto/', views.producto, name='producto'),
    path('Proveedor/', views.proveedor, name='proveedor'),
    path('Rol/', views.rol, name='Rol'),
    path('TipoProducto/', views.tipoprod, name='tipoprod'),
    path('usuario/', views.usuario, name='usuario'),
    path('usuario/registro', views.register, name='register'),
    path('Ventas/', views.ventas, name='Ventas'),
    path('login/', views.login_view, name='login'),
    path('lacteos/', views.lacteos, name='lacteos'),
    path('licores/', views.licores, name='licores'),
    path('aseo/', views.aseo, name='aseo'),
    path('despensa/', views.despensa, name='despensa'),
    path('golosinas/', views.golosinas, name='golosinas'),
    path('intento/', views.intento, name='intento'),
    path('menu/', views.menu, name='menu')
]

