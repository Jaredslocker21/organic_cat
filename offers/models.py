from django.db import models
from django.contrib.auth.models import User


class Offers(models.Model):
    """
    Product Offer Model
    """
    slider_img1 = models.ImageField(null=True, blank=True)
    slider_img2 = models.ImageField(null=True, blank=True)
    slider_img3 = models.ImageField(null=True, blank=True)
    caption1 = models.CharField(max_length=254)
    caption2 = models.CharField(max_length=254)
    caption3 = models.CharField(max_length=254)

    def __str__(self):
        return str(self.caption1)

    def __str__(self):
        return str(self.caption2)

    def __str__(self):
        return str(self.caption3)
