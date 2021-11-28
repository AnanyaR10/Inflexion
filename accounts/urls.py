from django.test import TestCase

# Create your tests here.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out, name="log_out"),
    path('registration/', views.registration, name="register"),
    path('create_orders/', views.create_orders, name="create_orders")
]
