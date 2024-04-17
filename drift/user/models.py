from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):

    name = models.CharField(max_length=50)
    adress = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')
    phone = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name