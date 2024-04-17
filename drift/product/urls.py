from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static,settings
from . import views

urlpatterns = [
    path('', views.category_wise,name='home'),
    path('products_display',views.product_display,name='product_display'),
    path('product_des/<int:id>/',views.product_desc,name='product_description')

]