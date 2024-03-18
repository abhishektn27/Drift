from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static,settings
from . import views

urlpatterns = [
    path('', views.index,name='home'),

]