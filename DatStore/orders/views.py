from django.shortcuts import render
from .utils import get_or_create_order
from carts.utils import get_or_create_cart
from .utils import breadcrumb
from django.contrib import messages
from .models import Order

from django.contrib.auth.decorators import login_required

@login_required
def order(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    return render(request, 'orders/order.html', {
        'cart': cart,
        'order': order,
        'breadcrumb':breadcrumb()
    })

@login_required
def address(request):

    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    shipping_address=order.get_or_set_shipping_address()

    return render(request, 'orders/address.html', {
        'cart': cart,
        'order': order,
        'shipping_address': shipping_address,
        'breadcrumb':breadcrumb(address=True)

    })

@login_required
def select_address(request):
    return render(request, 'orders/select_address.html')