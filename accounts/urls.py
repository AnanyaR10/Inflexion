from django.test import TestCase

# Create your tests here.
from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
  
urlpatterns = [
    path('', views.landing, name="landing"),
    path('upload_image/', views.image_upload, name="image_upload"),
    path('login/', views.log_in, name="login"),
    path('registration/', views.registration, name="register"),
    path('adminPage/', views.admin, name="admin"),
    path('logout/', views.log_out, name="log_out"),
    path('create_orders/', views.create_orders, name="create_orders"),
    path('user/', views.userPage, name="userPage" )
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

"""

urlpatterns = [
    path('', views.landing, name="landing"),
    #path('', views.home, name="home"),
    path('products/', views.products),
    path('customer/', views.customer),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out, name="log_out"),
    path('registration/', views.registration, name="register"),
    path('create_orders/', views.create_orders, name="create_orders"),
    path('user/', views.userPage, name="userPage" )
]
"""