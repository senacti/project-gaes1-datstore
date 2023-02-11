from django.db import models

from core.models import Product

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    products = models.ManyToManyField(Product, blank=True, verbose_name="Productos")

    def __str__(self):
        return self.name