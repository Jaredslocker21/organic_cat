from django.test import TestCase
from .forms import OrderForm


class OrderFormTest(TestCase):

    def full_name_test_required(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def email_required_test(self):
        form = OrderForm(
            {
                'full_name': 'A Name',
                'email': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def phone_number_required_test(self):
        form = OrderForm(
            {
                'full_name': 'A Name',
                'email': 'email@email.com',
                'phone_number': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def street_address1_required_test(self):
        form = OrderForm(
            {
                'full_name': 'A Name',
                'email': 'email@email.com',
                'phone_number': '1234567890',
                'street_address1': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')

    def city_or_town_required_test(self):
        form = OrderForm(
            {
                'full_name': 'A Name',
                'email': 'email@email.com',
                'phone_number': '1234567890',
                'street_address1': '123 street',
                'town_or_city': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def country_required_test(self):
        form = OrderForm(
            {
                'full_name': 'A Name',
                'email': 'email@email.com',
                'phone_number': '1234567890',
                'street_address1': '123 street',
                'town_or_city': 'anytown',
                'country': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(
            form.errors['country'][0], 'This field is required.')

    def street_address2_required_test(self):
        form = OrderForm(
            {
                'full_name': 'A Name',
                'email': 'email@email.com',
                'phone_number': '1234567890',
                'street_address1': '123 street',
                'town_or_city': 'anytown',
                'country': 'SW',
            })
        self.assertTrue(form.is_valid)