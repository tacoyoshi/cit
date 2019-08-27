from django.db import models
from serials.models import Serial

# Create your models here.

class Project(models.Model):
    serial = models.ManyToManyField(Serial, blank=True)
    project_code = models.CharField(max_length=20, unique=True)
    project_name = models.CharField(max_length=100)
    project_created = models.DateField(auto_now_add=True, verbose_name='Date Created')

    def __str__(self):
        return  self.project_code + ' - ' + self.project_name

    class Meta:
        ordering = ["project_code"]
        get_latest_by = ['rev_created']
        verbose_name = 'Revision'
        verbose_name_plural = 'Revisions'

    class Meta:
        ordering = ['-project_created']
        get_latest_by = ['-project_created']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
