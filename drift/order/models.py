from django.db import models

from user.models import Customer
from product.models import Products






# Create your models here.

class Order(models.Model):
    LIVE=1
    DELETE= 0
    DELETE_CHOICE=((LIVE,'live'),(DELETE, 'delete'))
    cart_stage=0
    order_confirmed=1
    order_processed=2
    order_delivered=3
    order_rejected=4
    status_choice=((order_confirmed,'order_confirmed'),
                   (order_processed,'order_processed'),
                   (order_delivered,'order_delivered'),
                   (order_delivered,'order_rejected')
    )

    order_status=models.IntegerField(choices=status_choice,default=cart_stage)
    owner= models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



class OrderdItem(models.Model):
    product=models.ForeignKey(Products,related_name='added_carts',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')