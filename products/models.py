from django.db import models

# Create your models here.

class Product(models.Model):
    product_code = models.CharField(max_length=3, unique=True)
    product_name = models.CharField(max_length=50)
    def __str__(self):
        return self.product_code + ' - ' + self.product_name
    class Meta:
        ordering = ["product_code"]
