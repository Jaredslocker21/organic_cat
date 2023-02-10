from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.


def checkout(request):
    """ A view to return the index page """
    cart = request.session.get('cart')
    if not cart:
        message.error(request, 'There is nothing in you cart.')
        return redirect(reverse('products'))

        order_form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            }

    return render(request, 'checkout/checkout.html')