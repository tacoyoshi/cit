from django.db import models
from serials.models import Serial

# Create your models here.

class Project(models.Model):
    serial = models.ForeignKey(Serial, on_delete=models.SET_NULL, blank=True, null=True)
    project_code = models.CharField(max_length=20, unique=True)
    project_name = models.CharField(max_length=100)
    def __str__(self):
        return  self.project_code + ' - ' + self.project_name
