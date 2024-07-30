from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from addressbookapp.views import RegisterView

urlpatterns = [
    path('', views.addressbook_list, name='addressbook_list'),
    path('create/', views.addressbook_create, name='addressbook_create'),
    path('update/<int:pk>/', views.addressbook_update, name='addressbook_update'),   
    #path('addressbook/<int:pk>/update/', views.addressbook_update, name='addressbook_update'),
    path('delete/<int:pk>/', views.addressbook_delete, name='addressbook_delete'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
#'AddressBook_update'