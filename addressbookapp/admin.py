from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AddressBook , State
 

admin.site.register(AddressBook)
admin.site.register(State)