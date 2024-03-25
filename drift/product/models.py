from django.db import models


# Create your models here.

# creating category models
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/', default='')

    def __str__(self):
        return '{}'.format(self.name)


class Products(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.IntegerField(max_length=100)
    image = models.ImageField(upload_to='media/')
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.title)
