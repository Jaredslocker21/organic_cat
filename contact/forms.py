from django import forms
from .models import ContactForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = (
            'description',
            'contact_name',
            'contact_email',
            'contact_phone_number',
            'contact_message',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders,
        remove auto-generated labels
        set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'contact_name': 'Full Name',
            'contact_email': 'Email Address',
            'contact_phone_number': 'Phone Number',
            'contact_message': 'Message',
        }

        self.fields['contact_name'].widget.attrs['autofocus'] = True
