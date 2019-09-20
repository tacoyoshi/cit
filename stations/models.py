from django.db import models
from django.urls import reverse

# Create your models here.

class Station(models.Model):
    station_code = models.CharField(max_length=3, unique=True)
    station_name = models.CharField(max_length=50)

    def __str__(self):
        return self.station_code + ' - ' + self.station_name

    def get_absolute_url(self):
        return reverse('station-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['station_code']
        verbose_name = 'Station'
        verbose_name_plural = 'Stations'
