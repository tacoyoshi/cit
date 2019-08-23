from django.db import models
from stations.models import Station

# Create your models here.

class Serial(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=4)
    def __str__(self):
        return self.serial_number
