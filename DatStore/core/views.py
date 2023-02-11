from unicodedata import category
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.db.models import Q
from shipping_addresses.models import ShippingAddress
from core.models import Product, InventoryEntry,EntryDetail, TypeProduct
from carts.models import Cart,CartProducts
from orders.models import Order,Delivery
from orders.common import OrderStatus
from .forms import InventoryEntry
from django.contrib.auth.decorators import login_required
from .forms import EntInvForm,DetEntInvForm,OrderDelForm,ProductForm,TipProdForm
from django.db.models import CharField, Value
from django.db.models.functions import Concat
from users.models import User
from core.models import Supplier
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group 
from django.contrib.auth.decorators import user_passes_test


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            return view_func(request,*args,**kwargs)
        return wrapper_func
    return decorator

#CRUD-----------------------------

@login_required
def domicilio(request):
    if request.user.groups.filter(name='Empleado').exists():

        dom= Delivery.objects.all()
    
        if request.method == 'GET':
            return render(request, "Domicilio.html", {
                'dom':dom
            })
    else:
        return redirect('index')


@login_required
def Orders(request):
    ordenes= Order.objects.all().filter(status=OrderStatus.COMPLETED).order_by('-order_id')
    ordenpay= Order.objects.select_related('user').all().filter(status=OrderStatus.PAYED).order_by('-order_id')

    sql="select O.Id,user_id,u.phone,status,total,created_at from orders_order as O JOIN users_user u on o.user_id=u.id WHERE status='OrderStatus.PAYED';"

    prob=Order.objects.raw(sql)
    
    if request.method == 'GET':
        return render(request, "Orders.html", {
            'ordenes':ordenes,
            'ordenpay':ordenpay,
            'prob':prob
        })

@login_required
def OrderDel(request, pk):
    ordenc= get_object_or_404(Order, pk=pk)
    carp=CartProducts.objects.all().filter(cart=ordenc.cart)
    if request.method == 'GET':
        orden= get_object_or_404(Order, pk=pk)

        ship= ShippingAddress.objects.get(postal_code=orden.shipping_address)
        form=OrderDelForm(initial={'direction':orden.address,'price':orden.shipping_total,'idpedidoFK':orden.pk})

        ordv=orden.order_id

        return render(request, 'OrderDel.html',{'form':form,'ordv':ordv, 'carp':carp})
    else:
        try:
            orden= Order.objects.get(pk=pk)
            orden.status=OrderStatus.PAYED
            orden.save()
            #ordv=orden.order_id
            form=OrderDelForm(request.POST)
            deliv = form.save(commit=False)
            deliv.user = request.user
            deliv.save()
            return redirect('core:Orders')
        except:
            return render(request, 'OrderDel.html',{ 'form':form,
            'error': 'Datos invalidos','carp':carp})

@login_required
def Det_EntInv(request, pk):
    detenv= EntryDetail.objects.all().filter(identinvFK=pk)
    iddet= get_object_or_404(InventoryEntry, pk=pk)
    form= DetEntInvForm(initial={'identinvFK':iddet.pk})
    if request.method == 'GET':
        return render(request, "Det_EntInv.html", {
            'form': form,
            'detenv':detenv
        })
    else:
        try:
            form= DetEntInvForm(request.POST)
            new_detentinv = form.save(commit=False)

            prods=Product.objects.get(name=new_detentinv.idprodFK)
            prods.stock += new_detentinv.quantity
            prods.save()
            new_detentinv.save()

            grup=EntryDetail.objects.last()
            grup.groupcost =new_detentinv.quantity*new_detentinv.purchaseprice
            grup.save()

            tot=InventoryEntry.objects.get(pk=new_detentinv.identinvFK)
            tot.totalpurchase += grup.groupcost
            tot.save()

            return redirect('core:Ent_Inventario')
        except ValueError:
            return render(request, "Det_EntInv.html", {
                'entradas':detenv,
                'form': DetEntInvForm,
                'error': 'Datos invalidos'
            })

@login_required
def det_ent_inv_det(request, pk):
    if request.method == 'GET':
        detentrada= get_object_or_404(EntryDetail, pk=pk)
        form = DetEntInvForm(instance=detentrada)
        return render(request, 'det_ent_inv_det.html',{'detentrada':detentrada, 'form':form})
    else:
        try:
            detentrada=get_object_or_404(EntryDetail, pk=pk)
            form=DetEntInvForm(request.POST,instance=detentrada)
            form.save()
            return redirect('core:Ent_Inventario')
        except:
            return render(request, 'det_ent_inv_det.html',{'detentrada':detentrada, 'form':form,
            'error': 'Datos invalidos'})

@login_required
def elim_det_ent_inv(request, pk):
    entrada= get_object_or_404(EntryDetail, pk=pk)
    if request.method=='POST':

        prods=Product.objects.get(name=entrada.idprodFK)
        prods.stock-= entrada.quantity
        prods.save()

        tot=InventoryEntry.objects.get(pk=entrada.identinvFK)
        tot.totalpurchase-= entrada.groupcost
        tot.save()
        entrada.delete()
        return redirect('core:Ent_Inventario')


@login_required
def Ent_Inventario(request):
    entradas= InventoryEntry.objects.all().order_by('-pk')
    form= EntInvForm()
    if request.method == 'GET':
        return render(request, "Ent_Inventario.html", {
            'form': EntInvForm,
            'entradas':entradas
        })
    else:
        try:
            form= EntInvForm(request.POST)
            new_entinv = form.save(commit=False)
            new_entinv.iduser = request.user
            new_entinv.save()
            return redirect('core:Ent_Inventario')
        except ValueError:
            return render(request, "Ent_Inventario.html", {
                'entradas':entradas,
                'form': EntInvForm,
                'error': 'Datos invalidos'
            })

@login_required
def ent_inv_det(request, pk):
    if request.method == 'GET':
        entrada= get_object_or_404(InventoryEntry, pk=pk)
        form = EntInvForm(instance=entrada)
        return render(request, 'ent_inv_det.html',{'entrada':entrada, 'form':form})
    else:
        try:
            entrada=get_object_or_404(InventoryEntry, pk=pk, user=request.user)
            form=EntInvForm(request.POST,instance=entrada)
            form.save()
            return redirect('core:Ent_Inventario')
        except:
            return render(request, 'ent_inv_det.html',{'entrada':entrada, 'form':form,
            'error': 'Datos invalidos'})

@login_required
def elim_ent_inv(request, pk):
    entrada= get_object_or_404(InventoryEntry, pk=pk)
    if request.method=='POST':
        entrada.delete()
        return redirect('core:Ent_Inventario')



#/CRUD----------------------------
class ProductSearchListViewCAT(ListView):
    template_name = 'TAseo.html'
    paginate_by = 8


    def get_queryset(self):
        idtip=self.request.GET.get('pp')
        return Product.objects.raw('''select * from Producto WHERE idfktipp_id = %s ''',[(idtip)])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de productos'
        return context





class ProductListView(ListView):
    template_name = 'TAseo.html'
    sql="select * from Producto;"
    queryset = Product.objects.raw(sql)#Product.objects.filter(idfktipp=5)
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de productos'
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'productos/producto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print(context)

        return context


class ProductSearchListView(ListView):
    template_name = 'productos/search.html'

    def get_queryset(self):
        filters = Q(name__icontains=self.query()) | Q(
            category__name__icontains=self.query())
        return Product.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['product_list'].count()

        return context

def invoice(request):
    return render(request, "invoice.html")

def report(request):
    datos = Supplier.objects.all()
    return render(request, "invoice.html", {"datos": datos})