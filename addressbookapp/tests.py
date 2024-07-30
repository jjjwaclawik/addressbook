from django.test import TestCase
from django.urls import reverse
from .models import AddressBook
from .forms import AddressForm

#  Unable to run unit tests with user field ' owner = models.ForeignKey(User,on_delete=models.CASCADE)'
#from addressbookapp.models import User, UserProfile
#from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin

# Create your tests here.

class addressbookTests(TestCase):

    def setUp(self):
        #create a user for testing
        #self.user1 = User.objects.create(username='user1')
        #self.up1 = UserProfile.objects.create(user=self.user1)
        self.AddressBook = AddressBook.objects.create(
            name='A Test Addressee',
            address1='1 Main Street',
            address2='Apartment 01A',
            city='Millis',
            state='MA',
            zipcode='02054',
            owner='1',
        )
  
    def test_addressbook_list_view(self):
        response = self.client.get(reverse('addressbook_list'))
        self.assertEqual(response.status_code, 200)  #200 = successful page load
        self.assertContains(response, 'A Test Addressee')
        self.assertTemplateUsed(response, 'addressbookapp/addressbook_list.html')

    def test_addressbook_create_view(self):
        addressbook_count = AddressBook.objects.count()
        response = self.client.post(reverse('addressbook_create'), {
            'name' : 'A Test Addressee',
            'address1' : '1 Main Street',
            'address2' : 'Apartment 01A',
            'city' : 'Millis',
            'state' : 'MA',
            'zipcode' : '02054',
            'owner' : '1',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertEqual(AddressBook.objects.count(), addressbook_count + 1)
        self.assertEqual(self.AddressBook.name, 'A Test Addressee')
        self.assertEqual(self.AddressBook.address1, '1 Main Street')
        self.assertEqual(self.AddressBook.address2, 'Apartment 01A')
        self.assertEqual(self.AddressBook.city, 'Millis')
        self.assertEqual(self.AddressBook.state, 'MA')
        self.assertEqual(self.AddressBook.zipcode, '02054')                 
        self.assertEqual(self.AddressBook.owner, '1')  

    def test_addressbook_update_view(self):
        response = self.client.post(reverse('addressbook_update', args=[self.AddressBook.id]), {
            'name' : 'An Updated Test Addressee',
            'address1' : '2B Main Street',
            'address2' : 'Apartment 02B',
            'city' : 'Medway',
            'state' : 'GA',
            'zipcode' : '02053',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after update
        self.AddressBook.refresh_from_db()
        self.assertEqual(self.AddressBook.name, 'An Updated Test Addressee')
        self.assertEqual(self.AddressBook.address1, '2B Main Street')
        self.assertEqual(self.AddressBook.address2, 'Apartment 02B')
        self.assertEqual(self.AddressBook.city, 'Medway')
        self.assertEqual(self.AddressBook.state, 'GA')
        self.assertEqual(self.AddressBook.zipcode, '02053')  

    def test_addressbook_delete_view(self):
        addressbook_count = AddressBook.objects.count()
        response = self.client.post(reverse('addressbook_delete', args=[self.AddressBook.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after deletion
        self.assertEqual(AddressBook.objects.count(), addressbook_count - 1)
        self.assertFalse(AddressBook.objects.filter(id=self.AddressBook.id).exists())


class addressbookModelTests(TestCase):

    def test_addressbook_creation(self):
        addressbook = AddressBook.objects.create(
            title='Test addressbook',
            author='Test Author',
            genre='Test Genre',
            url='https://djangoproject.com',
        )
        self.assertEqual(self.AddressBook.title, 'Test addressbook')
        self.assertEqual(self.AddressBook.author, 'Test Author')
        self.assertEqual(self.AddressBook.genre, 'Test Genre')
        self.assertEqual(self.AddressBook.url, 'https://djangoproject.com')


class addressbookModelTests(TestCase):

    def test_addressbook_creation(self):
        addressbook = AddressBook.objects.create(
            title='Test addressbook',
            author='Test Author',
            genre='Test Genre',
            url='https://testaddressbook.com'
        )
        self.assertEqual(addressbook.title, 'Test addressbook')
        self.assertEqual(addressbook.author, 'Test Author')
        self.assertEqual(addressbook.genre, 'Test Genre')
        self.assertEqual(addressbook.url, 'https://testaddressbook.com')

class AddressFormTests(TestCase):

    def test_valid_form(self):
        data = {
            'name' : 'A Test Addressee',
            'address1' : '1 Main Street',
            'address2' : 'Apartment 01A',
            'city' : 'Millis',
            'state' : 'MA',
            'zipcode' : '02054',
            'owner' : '1',
        }
        form = AddressForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'name' : 'A Test Addressee',
            'address1' : '',
            'address2' : 'Apartment 01A',
            'city' : 'Millis',
            'state' : 'MAAAA',
            'zipcode' : '0205402054020540205402054',
            'owner' : '1',
        }  #address 1 must not be blank
        form = AddressForm(data=data)
        self.assertFalse(form.is_valid())