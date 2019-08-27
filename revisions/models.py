from django.db import models
from parts.models import Part
from projects.models import Project
from serials.models import Serial
from options.models import Option
from datetime import date

# Create your models here.

class Revision(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE, verbose_name='Part')
    rev_number = models.CharField(max_length=12, verbose_name='Revision')
    rev_control_number = models.PositiveIntegerField(default=0, verbose_name='Control Number')
    rev_created = models.DateField(auto_now_add=True, verbose_name='Date Created')
    rev_effective = models.DateField(blank=True, null=True, verbose_name='Effective Date')
    rev_ed_code = models.CharField(max_length=8, blank=True, verbose_name='ED Code')
    rev_description = models.CharField(max_length=200, blank=True, verbose_name='Description')
    rev_notes = models.TextField(blank=True, verbose_name='Revision Notes')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Project')
    serial = models.ForeignKey(Serial, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Serial Effectivity')
    option = models.ForeignKey(Option, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Option')

    def __str__(self):
        return self.part.part_number + ' - Rev ' + self.rev_number

    class Meta:
        ordering = ['part__part_number', '-rev_effective' , '-rev_number']
        get_latest_by = ['rev_created']
        verbose_name = 'Revision'
        verbose_name_plural = 'Revisions'
