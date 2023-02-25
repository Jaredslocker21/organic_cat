from django.contrib import admin
from .models import Reviews


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'name',
                    'body', 'created_on',
                    'posted_by', 'product')


admin.site.register(Reviews)
