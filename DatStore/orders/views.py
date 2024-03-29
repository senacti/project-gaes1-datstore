from django.shortcuts import render, get_object_or_404

import threading

from .utils import get_or_create_order
from .utils import breadcrumb
from .utils import destroy_order

from carts.utils import destroy_cart
from carts.utils import get_or_create_cart

from .models import Order
from django.contrib import messages

from django.shortcuts import redirect
from shipping_addresses.models import ShippingAddress

from .mails import Mail
from django.contrib.auth.decorators import login_required

from django.db.models.query import EmptyQuerySet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from .decorator import validate_cart_and_order


class OrderListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'orders/orders.html'

    def get_queryset(self):
        return self.request.user.orders_completed()


@login_required
@validate_cart_and_order
def order(request, cart, order):
    return render(request, 'orders/order.html', {
        'cart': cart,
        'order': order,
        'breadcrumb': breadcrumb()
    })


@login_required
@validate_cart_and_order
def address(request, cart, order):
    shipping_address = order.get_or_set_shipping_address()
    can_choose_address = request.user.shippingaddress_set.count() > 1

    return render(request, 'orders/address.html', {
        'cart': cart,
        'order': order,
        'shipping_address': shipping_address,
        'can_choose_address': can_choose_address,
        'breadcrumb': breadcrumb(address=True)

    })


@login_required
def select_address(request):
    shipping_addresses = request.user.addresses

    return render(request, 'orders/select_address.html', {
        'breadcrumb': breadcrumb(address=True),
        'shipping_addresses': shipping_addresses
    })


@login_required
@validate_cart_and_order
def check_address(request, cart, order, pk):
    shipping_address = get_object_or_404(ShippingAddress, pk=pk)

    if request.user.id != shipping_address.user_id:
        return redirect('carts:cart')

    order.update_shipping_address(shipping_address)

    return redirect('orders:address')


@login_required
@validate_cart_and_order
def confirm(request, cart, order):
    shipping_address = order.shipping_address
    
    if shipping_address is None:
        return redirect('orders:address')
    

    return render(request, 'orders/confirm.html', {
        'cart': cart,
        'order': order,
        'shipping_address': shipping_address,
        'breadcrumb': breadcrumb(address=True, confirmation=True)
    })


@login_required
@validate_cart_and_order
def cancel(request, cart, order):

    if request.user.id != order.user_id:
        return redirect('carts:cart')

    order.cancel()

    destroy_cart(request)
    destroy_order(request)

    messages.error(request, 'Orden cancelada')
    return redirect('index')


@login_required
@validate_cart_and_order
def complete(request, cart, order):
    if request.user.id != order.user_id:
        return redirect('carts:cart')

    order.complete()
    orderad = get_object_or_404(Order, order_id=order.order_id)
    orderad.address=order.shipping_address.direct
    orderad.save()

    thread = threading.Thread(target=Mail.send_complete_order, args=(
        order, request.user
    ))

    thread.start()

    (order, request.user)

    destroy_cart(request)
    destroy_order(request)

    messages.success(request, 'Compra completada exitosamente')
    return redirect('index')
