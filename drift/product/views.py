from django.shortcuts import render
from .models import Category,Products
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return render(request,'home.html' )


def category_wise(request):
    category = Category.objects.all()
    return render(request,'home.html',{'category':category})


#


def product_display(request):
    products = Products.objects.all()
    return render(request,'product.html',{'products':products})


def product_desc(request,id):
    product = Products.objects.get(id=id)
    context={'product':product}
    return render(request,'product_description.html',context)