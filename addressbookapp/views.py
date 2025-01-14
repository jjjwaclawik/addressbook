from django.shortcuts import render, redirect, get_object_or_404
from .models import AddressBook
from .forms import AddressForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseForbidden
#  import http

def addressbook_list(request):
    addressbook = AddressBook.objects.all()
    return render(request, 'addressbookapp/addressbook_list.html', {'addressbook':addressbook})

@login_required
def addressbook_create(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addressbook_list')
    else:
        form = AddressForm()
    return render(request, 'addressbookapp/addressbook_form.html', {'form': form})

@login_required
def addressbook_update(request, pk):
    addressbook = get_object_or_404(AddressBook, pk=pk)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=addressbook)
        if form.is_valid():
            form.save()
            return redirect('addressbook_list')
    else:
        form = AddressForm(instance=addressbook)
    return render(request, 'addressbookapp/addressbook_form.html', {'form': form})

@login_required
def addressbook_delete(request, pk):
    address = get_object_or_404(AddressBook, pk=pk)
    if (address.owner != request.user ):
        return HttpResponseForbidden("You are not allowed to delete other Authors's work")
   
    if request.method == 'POST':
        address.delete()
        return redirect('addressbook_list')
    print(address.name)
    return render(request, 'addressbookapp/addressbook_confirm_delete.html' , {'address' : address})

   # return render(request, 'addressbookapp/addressbook_confirm_delete.html', {'address': address})

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'