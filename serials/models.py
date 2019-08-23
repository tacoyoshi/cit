from django.db import models
from stations.models import Station

# Create your models here.

class Serial(models.Model):
    K100 = '100'
    K200 = '200'
    AIRCRAFT_CHOICES = [
        (K100, "Kodiak 100"),
        (K200, "Kodiak 200")
    ]
    aircraft = models.CharField(max_length=3, choices=AIRCRAFT_CHOICES, default=K100)
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True)
    serial_number = models.CharField(max_length=4, unique=True)
    def __str__(self):
        return  self.aircraft + '-' + self.serial_number + '-' + self.station.station_code
