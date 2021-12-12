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
from .forms import OrderForm, CreateUserForm, Log_in_form,PictureForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, admin_only, allowed_users
from django.contrib.auth.models import Group
# Create your views here.

#@admin_only
#@login_required(login_url='login')
"""
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    context = {'orders': orders, 'customers': customers}
    return render(request, 'home.html', context)

"""

def landing(request):
       return render(request, 'landing.html')

@login_required(login_url='login')
def image_upload(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            print('check form validation')
            form.instance.user = request.user
            form.save()
            img_obj = form.instance
            return render(request, 'image_upload.html', {'form': form, 'img_obj': img_obj})
            #return redirect('userPage')
    else:
        id = request.user
        form = PictureForm()
    return render(request, 'image_upload.html', {'form' : form, 'id': id})



@login_required(login_url='login')
@admin_only
def admin(request):
    return render(request, 'admin.html')



@unauthenticated_user  # logged in users can't access
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
            return redirect('admin')
    context = {'form': form}
    return render(request, 'login.html', context)


@login_required(login_url='login')
def log_out(request):
    logout(request)
    return redirect('landing')
    #return redirect('login')

@login_required(login_url='login')
def userPage(request):
    allimages = Pictures.objects.all() 
    #phone=request.user.customer.phone
    #context={'phone':phone}
    return render(request, 'user_login.html', {'images':allimages})

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
@allowed_users(allowed_roles=['Customer'])
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

