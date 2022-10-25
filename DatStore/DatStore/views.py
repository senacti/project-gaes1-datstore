from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse
from core.models import Product
from django.contrib.auth.models import User

from DatStore.forms import RegisterForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html', {

    })

# LOGINCONF

# //LOGINCONF


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada correctamente')
    return redirect('login')


def index(request):
    products = Product.objects.all().order_by('-id')

    return render(request, 'index.html', {
        'message': 'Catalogo',
        'title': 'Productos',
        'products': products,
    })


def compras(request):
    return render(request, "Compras.html")


def detallePed(request):
    return render(request, "Det_Ped_inv.html")


def domicilio(request):
    return render(request, "Domicilio.html")


def estado(request):
    return render(request, "Estado.html")


def formaPago(request):
    return render(request, "Forma_pago.html")


def graficos(request):
    return render(request, "Graficos.html")


def inventario(request):
    return render(request, "Inventario.html")


def pedido(request):
    return render(request, "Pedido.html")


def producto(request):
    return render(request, "Producto.html")


def proveedor(request):
    return render(request, "Proveedor.html")


def rol(request):
    return render(request, "Rol.html")


def tipoprod(request):
    return render(request, "Tipo_prod.html")


def usuario(request):
    return render(request, "usuario.html")


def ventas(request):
    return render(request, "Ventas.html")


def lacteos(request):
    return render(request, "TLacteos.html")


def licores(request):
    return render(request, "TLicores.html")


def aseo(request):

    products = Product.objects.all().order_by('-id')

    return render(request, 'TAseo.html', {
        'message': 'Catalogo',
        'tittle' : 'Productos',
        'products': products,
    })


def despensa(request):
    return render(request, "TDespensa.html")

def golosinas(request):
    return render(request, "TGolosinas.html")

def intento(request):
    return render(request, "base.html")



def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = User.objects.create_user(username, email, password)
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')

            return redirect('index')
    return render(request, 'register.html', {
        'form': form
    })
