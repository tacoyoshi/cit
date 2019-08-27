from django.db import models

# Create your models here.

class Option(models.Model):
    option_code = models.CharField(max_length=3, unique = True)
    option_name = models.CharField(max_length=100, unique = True)

    def __str__(self):
        return self.option_code + ' - ' + self.option_name

    class Meta:
        ordering = ["option_code"]
        verbose_name = 'Option'
        verbose_name_plural = 'Options'
