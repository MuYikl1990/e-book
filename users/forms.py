from django import forms
from .models import Passport, Address

class PassportForm(forms.ModelForm):
    class Meta:
        model = Passport
        fields = ['username', 'password', 'email', 'is_active']
        labels = {'username': 'username', 'password': 'password', 'email': 'email', 'is_active': 'is_active'}

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['recipient_name', 'recipient_addr', 'zip_code', 'recipient_phone', 'is_default']
        labels = {'recipient_name': '', 'recipient_addr': '',  'zip_code': '', 'recipient_phone': '', 'is_default': ''}