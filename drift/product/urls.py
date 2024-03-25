from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static,settings
from . import views

urlpatterns = [
    path('', views.category_wise,name='home'),
    path('products/',views.product_display,name='product_display')

]