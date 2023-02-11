from django.forms import  ModelForm
from django.contrib.admin.widgets import AutocompleteSelect
from .models import InventoryEntry,EntryDetail, Product,TypeProduct
from orders.models import Delivery
from django.contrib import admin

class EntInvForm(ModelForm):
    class Meta:
        model = InventoryEntry
        fields=['refpayment','idwaytopay']

class DetEntInvForm(ModelForm):
    class Meta:
        model = EntryDetail
        fields=['quantity','purchaseprice','dateexpiry','idprodFK','identinvFK']
    widgets={
        'idprodFK':AutocompleteSelect(
            EntryDetail._meta.get_field('idprodFK').remote_field,
            admin.site,
            attrs={'placeholder':'seleccionar...'}
        )

    }

class OrderDelForm(ModelForm):
    class Meta:
        model = Delivery
        fields=['direction','idpedidoFK','price','deliver']

class ProductForm(ModelForm):
    class Meta:
        model= Product
        fields=['id','name','costp','stock','state','slug','image','idfksup','idfktipp']

class TipProdForm(ModelForm):
    class Meta:
        model= TypeProduct
        fields=['name']