from django.contrib import admin
from .models import Offers
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# @admin.register(Offers())
class OffersAdmin(admin.ModelAdmin):
    """
    This class displays a summernote model and  a nice list filter
    """
    list_display = (
        'free_delivery_threshold',
        'caption1',
        'caption2',
        'caption3',
    )    
    # summernote_fields = (
    #     'caption1',
    #     'caption2',
    #     'caption3',
    #     'slider_img1',
    #     'slider_img2',
    #     'slider_img3',
    #     'free_delivery_threshold',
    # )


admin.site.register(Offers)
