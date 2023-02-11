from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('search', views.ProductSearchListView.as_view(), name='search'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='producto'),
    path('Ent_Inventario/', views.Ent_Inventario, name='Ent_Inventario'),
    path('Det_EntInv/<int:pk>', views.Det_EntInv, name='Det_EntInv'),
    path('Det_EntInv_det/<int:pk>', views.det_ent_inv_det, name='det_ent_inv_det'),
    path('Det_EntInv/<int:pk>/delete', views.elim_det_ent_inv, name='elim_det_ent_inv'),
    path('Ent_Inventario_det/<int:pk>', views.ent_inv_det, name='ent_inv_det'),
    path('Ent_Inventario/<int:pk>/delete', views.elim_ent_inv, name='elim_ent_inv'),
    path('Orders/', views.Orders, name='Orders'),
    path('OrderDel/<int:pk>', views.OrderDel, name='OrderDel'),
    path('invoice', views.invoice, name='invoice'),
    path('Domicilio/', views.domicilio, name='domicilio'),
]