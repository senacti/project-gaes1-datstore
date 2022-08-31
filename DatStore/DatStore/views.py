from django.shortcuts import render

def index(request):
    return render(request, "index.html", {

    })

def compras(request):
    return render (request, "Compras.html") 

def detallePed(request):
    return render (request, "Det_Ped_inv.html") 

def domicilio(request):
    return render (request, "Domicilio.html")

def estado(request):
    return render (request, "Estado.html")  

def formaPago(request):
    return render (request, "Forma_pago.html")

def graficos(request):
    return render (request, "Graficos.html")

def inventario(request):
    return render (request, "Inventario.html")

def pedido(request):
    return render (request, "Pedido.html")

def producto(request):
    return render (request, "Producto.html")

def proveedor(request):
    return render (request, "Proveedor.html")

def rol(request):
    return render (request, "Rol.html")

def tipoprod(request):
    return render (request, "Tipo_prod.html")

def usuario(request):
    return render (request, "Usuario.html")

def ventas(request):
    return render (request, "Ventas.html")