from django.forms import ModelForm
from .models import ShippingAddress

class ShippingAddressForm(ModelForm):
    class Meta:
        model= ShippingAddress
        fields=[
            'line1' ,'postal_code','reference'
        ]
        labels ={
            'line1':'Dirección',
            'reference':'Referencias',
            'postal_code':'Codigo postal',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['line1'].widget.attrs.update({
            'class':'form-control'
        }) #Dic
        
        self.fields['reference'].widget.attrs.update({
            'class':'form-control'
        })

        self.fields['postal_code'].widget.attrs.update({
            'class':'form-control'
        }) #Dic

        