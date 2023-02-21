from django.shortcuts import render
from offers.models import Offers


# Create your views here.


def index(request):
    """ A view to return the index page """
    offers = Offers.objects.all()
    context = {
        'offers': offers[0],
        'free_delivery_threshold': offers[0].free_delivery_threshold
    }
    return render(request, 'home/index.html', context)