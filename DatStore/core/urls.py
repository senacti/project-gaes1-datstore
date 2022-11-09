from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('search', views.ProductSearchListView.as_view(), name='search'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='producto'),
    path('Ent_Inventario/', views.Ent_Inventario, name='Ent_Inventario'),
]