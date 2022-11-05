import imp
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.urls import include
from core.views import ProductListView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views     
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
    path('Ventas/', views.ventas, name='Ventas'),
    path('login/', views.login_view, name='login'),
    path('lacteos/', views.lacteos, name='lacteos'),
    path('licores/', views.licores, name='licores'),
    path('aseo/', ProductListView.as_view(), name='aseo'),
    path('despensa/', views.despensa, name='despensa'),
    path('golosinas/', views.golosinas, name='golosinas'),
    path('intento/', views.intento, name='intento'),
    path('usuario/', views.usuario, name='usuario'),
    path('productos/', include('core.urls')),
    path('carrito/', include('carts.urls')),
    path('usuario/', include('users.urls')),
    path('reset_password/',auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "DatStore.views.Error_404"