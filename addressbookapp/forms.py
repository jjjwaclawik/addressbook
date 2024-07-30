from django import forms
from .models import AddressBook

class AddressForm(forms.ModelForm):
    class Meta:
        model = AddressBook
        fields = ['name', 'address1', 'address2', 'city', 'state', 'zipcode', 'owner']
