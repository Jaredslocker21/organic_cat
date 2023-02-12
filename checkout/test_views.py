from django.test import TestCase
from .forms import OrderForm


class TestCheckoutViews(TestCase):

    def test_get_checkout_with_empty_cart(self):

        response = self.client.get('/checkout')
        self.assertTrue(response, '/products')