from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
    """
    creates a Review form
    """
    class Meta:
        model = Reviews
        fields = ['body',]