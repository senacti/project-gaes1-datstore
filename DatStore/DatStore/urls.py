import imp
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.urls import include
from core.views import ProductListView,ProductSearchListViewCAT
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
    path('Estado/', views.estado, name='estado'),
    path('FormaPago/', views.formaPago, name='formapago'),
    path('reportes/', views.graficos, name='reportes'),
    path('Pedido/', views.pedido, name='pedido'),
    path('Producto/', views.producto, name='producto'),
    path('Proveedor/', views.proveedor, name='proveedor'),
    path('Rol/', views.rol, name='Rol'),
    path('TipoProducto/', views.tipoprod, name='tipoprod'),
    path('Ventas/', views.ventas, name='Ventas'),
    path('login/', views.login_view, name='login'),
    path('lacteos/', ProductListView.as_view(), name='lacteos'),
    path('licores/', ProductListView.as_view(), name='licores'),
    path('aseo/', ProductListView.as_view(), name='aseo'),
    path('despensa/', ProductListView.as_view(), name='despensa'),
    path('golosinas/', ProductSearchListViewCAT.as_view(), name='golosinas'),
    path('intento/', views.intento, name='intento'),
    path('usuario/', views.usuario, name='usuario'), 
    path('contacto', views.contacto, name='contacto'),
    path('productos/', include('core.urls')),
    path('carrito/', include('carts.urls')),
    path('usuario/', include('users.urls')),
    path('orden/', include('orders.urls')),
    path('pagos/', include('billing_profiles.urls')),
    path('direcciones/', include('shipping_addresses.urls')),
    path('codigos/', include('promo_codes.urls')),
    path('reset_password/',auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("", include("allauth.urls")),
    path('pdf/', views.PDFView.as_view(), name='PDFView'), 
    path('form/', views.form, name='form'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "DatStore.views.Error_404"