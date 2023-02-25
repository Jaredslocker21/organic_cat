from django.shortcuts import render
from offers.models import Offers


# Create your views here.


def index(request):
    """ A view to return the index page """
    offers = Offers.objects.all()
    context = {
        'offers': offers[0],
    }
    return render(request, 'home/index.html', context)


def delivery(request):
    """
    View that returns the delivery policy page
    """
    return render(request, "home/delivery.html")


def privacy(request):
    """
    View that returns the privacy policy page
    """
    return render(request, "home/privacy.html")


def terms(request):
    """
    View that returns the terms policy page
    """
    return render(request, "home/terms.html")
