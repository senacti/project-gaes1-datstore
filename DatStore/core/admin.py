from email.mime import image
from django.contrib import admin
from users.models import Profile

from core.models import Delivery, DetOrder, EntryDetail, InventoryEntry, Inventoryoutput, Order, Permission, Product, Rol, Supplier, TypeProduct, Users, WayToPay

admin.site.register(TypeProduct);
admin.site.register(Supplier);
admin.site.register(Rol);
admin.site.register(Permission);
admin.site.register(WayToPay);
admin.site.register(Users);
admin.site.register(InventoryEntry);
admin.site.register(Profile);


class ProductAdmin(admin.ModelAdmin):
    fields = ('id', 'name','costp', 'stock', 'state', 'idfksup', 'idfktipp', 'image')
    list_display = ('__str__', 'slug', 'image')

admin.site.register(Product, ProductAdmin);

admin.site.register(EntryDetail);
admin.site.register(Order);
admin.site.register(DetOrder);
admin.site.register(Inventoryoutput);
admin.site.register(Delivery);