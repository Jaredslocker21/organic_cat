from django.shortcuts import render

# Create your views here.


def checkout(request):
    """ A view to return the index page """

    return render(request, 'checkout/checkout.html')