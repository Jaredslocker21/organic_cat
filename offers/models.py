from django.db import models
from django.contrib.auth.models import User


class Offers(models.Model):
    """
    Product Offer Model
    """
    #video = models.FileField(upload_to='media', null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    free_delivery_threshold = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        default=0,
    )
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

    def __str__(self):
        return str(self.free_delivery_threshold)