from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path ('staff_registration_form', views.staff_registration_form, name='staff_registration_form'),
    path ('customer_registration_form', views.staff_registration_form, name='customer_registration_form'),
]