from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
    """
    Review Form
    """
    class Meta:
        model = Reviews
        exclude = ('product', 'posted_by',)