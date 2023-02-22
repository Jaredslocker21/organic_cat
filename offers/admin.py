from django.contrib import admin
from .models import Offers
from django_summernote.admin import SummernoteModelAdmin


class OffersAdmin(admin.ModelAdmin):
    """
    This class displays a summernote model and  a nice list filter
    """
    list_display = (
        'caption1',
        'caption2',
        'caption3',
    )


admin.site.register(Offers)
