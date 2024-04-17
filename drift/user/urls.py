from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static,settings
from . import views


urlpatterns=[
    path('accounts/',  views.show_account,name='accounts'),
    path('logout/', views.log_out, name='logout')

    ]