from django.shortcuts import render,redirect
from .models import Order,OrderdItem
from product.models import Products

# Create your views here.
def show_cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=Order.objects.get_or_create(
        owner=customer,
        order_status=Order.cart_stage
    )
    context={'cart':cart_obj}

    return render(request,'cart.html',context)

def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.cart_stage
        )
        product=Products.objects.get(pk=product_id)
        orderd_item=OrderdItem.objects.create(

            product=product,
            owner=cart_obj,
            quantity=quantity
        )
        return redirect('cart_page')

