from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField()
    short_description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products_images')

    def __str__(self):
        return self.name
