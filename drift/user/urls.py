from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static,settings
from . import views


urlpatterns=[
path('accounts/',  views.user_form,name='accounts')
    ]