from email.mime import image
from django.contrib import admin
from users.models import Profile

from core.models import Delivery, DetOrder, EntryDetail, InventoryEntry, Inventoryoutput, Order,\
     Permission, Product, Rol, Supplier, TypeProduct, Users, WayToPay

#admin.site.register(TypeProduct);
#admin.site.register(Supplier);
#admin.site.register(Rol);
#admin.site.register(Permission);
#admin.site.register(WayToPay);
#admin.site.register(Users);
#admin.site.register(InventoryEntry);
#admin.site.register(Profile);

@admin.register(Profile)
class ProfileAdmi(admin.ModelAdmin):
    list_display= ["sname","slastname","birthdate"]
    list_display_links= ["sname","slastname","birthdate"]
    list_filter=["sname","slastname","birthdate"]
    search_fields=["sname","slastname","birthdate"]

@admin.register(InventoryEntry)
class InventoryEntryadmin(admin.ModelAdmin):
    list_display=["date","refpayment","totalpurchase","iduser","idwaytopay"]
    list_display_links=["date","refpayment","totalpurchase","iduser","idwaytopay"]
    list_filter=["date","refpayment","totalpurchase","iduser","idwaytopay"]
    search_fields=["date","refpayment","totalpurchase","iduser","idwaytopay"]


@admin.register(TypeProduct)
class TypeProductAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    search_fields= ["name"]
    list_filter= ["name"]

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["name","phone","email","direction"]
    list_display_links = ["name","phone"]
    list_filter= ["name","phone","direction"]

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display= ["name"]
    list_display_links = ["name"]
    list_filter = ["name"]


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display= ["name"]
    list_display_links= ["name"]
    list_filter=["name"]
    list_per_page = 2


@admin.register(WayToPay)
class WayToPayAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter=["name"]

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display=["name","lastn"]
    list_display_links=["name","lastn"]
    list_filter=["name","names","lastn","lastns"]
    search_fields=["name"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=["name","costp","stock"]
    list_display_links=["name","costp","stock"]
    list_filter=["name","costp","stock"]


class ProductAdmin(admin.ModelAdmin):
    fields = ('name','costp', 'stock', 'state', 'idfksup', 'idfktipp', 'image')
    list_display = ('__str__', 'slug', 'image')

#admin.site.register(Product, ProductAdmin);

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=["refpay","date"]
    list_display_links=["refpay","date"]
    list_filter=["refpay","date"]

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display=["idPedidoFK","price","idEmpleadoFK"]
    list_display_links=["price","idPedidoFK","idEmpleadoFK"]
    list_display_links=["idPedidoFK","idEmpleadoFK"]

@admin.register(EntryDetail)
class EntryDetailAdmin(admin.ModelAdmin):
    list_display=["quantity","dateexpiry","purchaseprice","groupcost"]
    list_display_links=["quantity","dateexpiry","purchaseprice","groupcost"]
    list_filter=["quantity","dateexpiry","purchaseprice","groupcost"]
    search_fields=["quantity","dateexpiry"]

@admin.register(DetOrder)
class DetOrder (admin.ModelAdmin):
    list_display=["idfkord","quant","costgp","idfkprod"]
    list_display_links=["idfkord","quant","costgp","idfkprod"]
    list_filter=["idfkord","idfkprod","costgp"]
    search_fields=["idfkord","quant","costgp","idfkprod"]

@admin.register(Inventoryoutput)
class InventoryoutputAdmin (admin.ModelAdmin):
    list_display=["amount","dateout","idprofk","iddepefk"]
    list_display_links=["amount","dateout","idprofk","iddepefk"]
    list_filter=["amount","dateout","idprofk","iddepefk"]
    search_fields=["amount","dateout","idprofk","iddepefk"]

#admin.site.register(EntryDetail);
#admin.site.register(Order);
#admin.site.register(DetOrder);
#admin.site.register(Inventoryoutput);
#admin.site.register(Delivery);