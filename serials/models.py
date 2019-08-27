from django.db import models
from stations.models import Station
from products.models import Product

# Create your models here.

class Serial(models.Model):

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    serial_number = models.CharField(max_length=4, unique=True)
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, blank=True, null=True)

    def serial_code(self):
        if self.product is None:
           return self.station.station_code + '-' + self.serial_number
        elif self.station is None:
           return self.product.product_code + '-' + self.serial_number + '-' + '000'
        elif (self.product is None and self.station is None):
           return self.serial_number
        else:
           return self.product.product_code + '-' + self.serial_number + '-' + self.station.station_code

    def __str__(self):
        return self.serial_code()

    class Meta:
        ordering = ['product', 'serial_number', 'station']
        verbose_name = 'Serial'
        verbose_name_plural = 'Serials'
