from django.test import TestCase
from django.urls import reverse_lazy

# Create your tests here.
from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.landing, name="landing"),
    path('upload_image/', views.image_upload, name="image_upload"),
    path('login/', views.log_in, name="login"),
    path('registration/', views.registration, name="register"),
    path('adminPage/', views.admin, name="admin"),
    path('logout/', views.log_out, name="log_out"),
    path('create_orders/', views.create_orders, name="create_orders"),
    path('user/', views.userPage, name="userPage" ),

    path('reset_password/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done')), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_rest_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:password_reset_complete')), name="password_rest_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete")

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