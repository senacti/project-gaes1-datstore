from django.db import models

from core.models import Product

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.name