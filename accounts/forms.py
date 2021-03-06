from django.forms import ModelForm
from .models import Order,Pictures
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class PictureForm(ModelForm):
    class Meta:
        model = Pictures
        fields = ['pic', 'name']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class Log_in_form(AuthenticationForm):
    class Meta:
        model=User
        fields = ['username', 'password']
