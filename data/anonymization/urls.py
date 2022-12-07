from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('it_home/', views.it_home, name='it_home'),
    path('bank_home/', views.bank_home, name='bank_home'),
    path('it_profile/<int:pk>', views.it_profile, name='it_profile'),
    path('bank_profile/<int:pk>', views.bank_profile, name='bank_profile'),
    path('store_bank_profile/', views.store_bank_profile, name='store_bank_profile'),
    path('store_it_profile/', views.store_it_profile, name='store_it_profile'),
    path('shared_data/<int:pk>', views.shared_data, name='shared_data'),
    path('details_user/<int:pk>', views.details_user, name='details_user'),

]