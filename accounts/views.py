from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm, CreateUserForm, Log_in_form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm, CreateUserForm, Log_in_form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
# Create your views here.


@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    context = {'orders': orders, 'customers': customers}
    return render(request, 'home.html', context)


@unauthenticated_user
def log_in(request):
    form = Log_in_form()

    if request.method == 'POST':
        #form = Log_in_form(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print('logged in')
            login(request, user)
            return redirect('/')
    context = {'form': form}
    return render(request, 'login.html', context)


@login_required(login_url='login')
def log_out(request):
    logout(request)
    return redirect('/login')


def registration(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name='Customer')
                user.groups.add(group)
                messages.success(
                    request, 'Account was created for ' + username)
                return redirect('login')
            else:
                messages.info(request, 'Username Or password incorrect')
        context = {'form': form}
        return render(request, 'registration.html', context)


@login_required(login_url='login')
def products(request):
    return HttpResponse('products')


@login_required(login_url='login')
def customer(request):
    return HttpResponse('customers')


@login_required(login_url='login')
@admin_only
def create_orders(request):
    form = OrderForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_orders')

    context = {'form': form}
    return render(request, 'order.html', context)
