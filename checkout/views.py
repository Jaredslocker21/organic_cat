from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Product
from cart.contexts import cart_contents

import stripe
import json


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        #'stripe_public_key': pk_test_51MONKZGI7uwgP4VlGl87kPCKL6bl66FMcIawxKO8GrZumBFfvSxBSCYrxWx3nmUiXdHEGM8JIG5nGqxVUAc9kfw600v6IjMZAp,
        #'client_secret': 'test',
    }

    return render(request, template, context)