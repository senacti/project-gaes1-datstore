from django.forms import  ModelForm
from .models import InventoryEntry

class EntInvForm(ModelForm):
    class Meta:
        model = InventoryEntry
        fields=['date','totalpurchase','refpayment','idwaytopay']