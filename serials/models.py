from django.db import models
from stations.models import Station
from products.models import Product

# Create your models here.

class Serial(models.Model):
    K100 = '100'
    K200 = '200'
    AIRCRAFT_CHOICES = [
        (K100, "Kodiak 100"),
        (K200, "Kodiak 200")
    ]

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    serial_number = models.CharField(max_length=4, unique=True)
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, blank=True, null=True)

    def make_serial_code(self):
        if self.product is None:
           return self.station.station_code + '-' + self.serial_number
        elif self.station is None:
           return self.product.product_code + '-' + self.serial_number + '-' + '000'
        elif (self.product is None and self.station is None):
           return self.serial_number
        else:
           return self.product.product_code + '-' + self.serial_number + '-' + self.station.station_code

    def save(self, *args, **kwargs):
       self.serial_code = self.make_serial_code()
       super(Serial, self).save(*args, **kwargs)

    def __str__(self):
        # if self.product is None:
        #    return self.station.station_code + '-' + self.serial_number
        # elif self.station is None:
        #    return self.product.product_code + '-' + self.serial_number
        # elif (self.product is None and self.station is None):
        #    return self.serial_number
        # else:
        #    return self.product.product_code + '-' + self.serial_number + '-' + self.station.station_code
        return self.make_serial_code()

    class Meta:
        ordering = ["serial_number"]
