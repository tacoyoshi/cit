from django.db import models

# Create your models here.

class Product(models.Model):
    product_code = models.CharField(max_length=3, unique=True, verbose_name='Product Code')
    product_name = models.CharField(max_length=50, verbose_name='Product Name')

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['product_code']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
