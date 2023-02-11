from email.mime import image
from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.decorators import login_required
from core.models import  DetOrder, EntryDetail, InventoryEntry, Inventoryoutput, Order,\
      Product, Supplier, TypeProduct, Users, WayToPay

#admin.site.register(TypeProduct);
#admin.site.register(Supplier);
#admin.site.register(Permission);
#admin.site.register(WayToPay);
#admin.site.register(Users);
#admin.site.register(InventoryEntry);
#admin.site.register(Profile);


@admin.register(InventoryEntry)
class InventoryEntryadmin(ImportExportModelAdmin):
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
"""""
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=["name","costp","stock"]
    list_display_links=["name","costp","stock"]
    list_filter=["name","costp","stock"]
"""""

class ProductAdmin(ImportExportModelAdmin):
    fields = ('id','name', 'description', 'costp', 'stock', 'state', 'idfksup', 'idfktipp', 'image')
    list_display = ('__str__', 'slug', 'image')

admin.site.register(Product, ProductAdmin);

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display=["refpay","date"]
    list_display_links=["refpay","date"]
    list_filter=["refpay","date"]



@admin.register(EntryDetail)
class EntryDetailAdmin(ImportExportModelAdmin):
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
class InventoryoutputAdmin (ImportExportModelAdmin):
    list_display=["amount","dateout","idprofk","iddepefk"]
    list_display_links=["amount","dateout","idprofk","iddepefk"]
    list_filter=["amount","dateout","idprofk","iddepefk"]
    search_fields=["amount","dateout","idprofk","iddepefk"]

#admin.site.register(EntryDetail);
#admin.site.register(Order);
#admin.site.register(DetOrder);
#admin.site.register(Inventoryoutput);
#admin.site.register(Delivery);

class InventoryEntryResource(resources.ModelResource):
    class Meta:
        model = InventoryEntry
        fields = ("date","refpayment","totalpurchase","iduser","idwaytopay")
        #export_order = ("date","refpayment","totalpurchase","iduser","idwaytopay")

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('name','costp', 'stock', 'state', 'idfksup', 'idfktipp', 'image')
        #export_order = ('name','costp', 'stock', 'state', 'idfksup', 'idfktipp', 'image')

class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
        fields = ("refpay","date")
        #export_order = ("refpay","date")



class EntryDetailResource(resources.ModelResource):
    class Meta:
        model = EntryDetail
        fields = ("quantity","dateexpiry","purchaseprice","groupcost")
        #export_order = ("quantity","dateexpiry","purchaseprice","groupcost")

class InventoryoutputResource(resources.ModelResource):
    class Meta:
        model = Inventoryoutput
        fields = ("amount","dateout","idprofk","iddepefk")
        #export_order = ("amount","dateout","idprofk","iddepefk")
        

