from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.http import HttpResponse
from core.models import Product
#from django.contrib.auth.models import User
from users.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.template.loader import get_template



def contacto(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        template = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'message': message
        })
    
        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            [email, 'cjmiranda135@gmail.com']
        )
    
        email.fail_silently = False
        email.send()


    return render(request, 'contactos.html',{
        
    })

def Error_404(request, exception):
    return render(request, 'error404.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(
                request, 'Bienvenido {} que disfrutes tu estadía'.format(user.username))

            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])

            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html', {})

# LOGINCONF

# //LOGINCONF


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada correctamente')
    return redirect('login')

# REGISTERCONFIG


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
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'register.html', {
        'form': form
    })

# EROR 404


def index(request):
    products = Product.objects.all().order_by('-id')

    return render(request, 'index.html', {
        'message': 'Catalogo',
        'title': 'Productos',
        'products': products,
    })


@login_required
def compras(request):
    return render(request, "Compras.html")


@login_required
def detallePed(request):
    return render(request, "Det_Ped_inv.html")


@login_required
def domicilio(request):
    return render(request, "Domicilio.html")


@login_required
def estado(request):
    return render(request, "Estado.html")


@login_required
def formaPago(request):
    return render(request, "Forma_pago.html")


def graficos(request):
    return render(request, "Graficos.html")

@login_required
def pedido(request):
    return render(request, "Pedido.html")


def producto(request):
    return render(request, "Producto.html")


@login_required
def proveedor(request):
    return render(request, "Proveedor.html")


@login_required
def rol(request):
    return render(request, "Rol.html")


@login_required
def tipoprod(request):
    return render(request, "Tipo_prod.html")


def usuario(request):
    return render(request, "usuario.html")


@login_required
def ventas(request):
    return render(request, "Ventas.html")


def lacteos(request):

    products = Product.objects.all().order_by('-id')

    return render(request, "TLacteos.html", {
        'message': 'Catalogo',
        'tittle': 'Productos',
        'products': products,
    })


def licores(request):

    products = Product.objects.all().order_by('-id')

    return render(request, "TLicores.html", {
        'message': 'Catalogo',
        'tittle': 'Productos',
        'products': products,
    })


def aseo(request):

    products = Product.objects.all().order_by('-id')

    return render(request, 'TAseo.html', {
        'message': 'Catalogo',
        'tittle': 'Productos',
        'products': products,
    })


def despensa(request):

    products = Product.objects.all().order_by('-id')

    return render(request, "TDespensa.html", {
        'message': 'Catalogo',
        'tittle': 'Productos',
        'products': products,
    })


def golosinas(request):

    products = Product.objects.all().order_by('-id')

    return render(request, "TGolosinas.html", {
        'message': 'Catalogo',
        'tittle': 'Productos',
        'products': products,
    })


def intento(request):
    return render(request, "base.html")


