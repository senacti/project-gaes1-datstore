from django.contrib import admin

from core.models import Delivery, DetOrder, EntryDetail, InventoryEntry, Inventoryoutput, Order, Permission, Product, Rol, Supplier, TypeProduct, User, WayToPay

admin.site.register(TypeProduct);
admin.site.register(Supplier);
admin.site.register(Rol);
admin.site.register(Permission);
admin.site.register(WayToPay);
admin.site.register(User);
admin.site.register(InventoryEntry);
admin.site.register(Product);
admin.site.register(EntryDetail);
admin.site.register(Order);
admin.site.register(DetOrder);
admin.site.register(Inventoryoutput);
admin.site.register(Delivery);