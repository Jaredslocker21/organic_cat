from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Reviews(models.Model):
    """
    Product Review Model
    """

    title = models.CharField(max_length=200, unique=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=80)    
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    posted_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_added",
        null=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        order date created on
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        returns a string
        """
        return f"Comment {self.body} by {self.title}"
