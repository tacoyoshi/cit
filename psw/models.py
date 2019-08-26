from django.db import models
from parts.models import Part
from projects.models import Project

# Create your models here.

class Psw(Part):
    psw_number = models.PositiveIntegerField(unique=True, verbose_name='PSW Number')
    psw_created = models.DateField(auto_now_add=True, editable=False, verbose_name='Date Created')
    psw_requestor = models.EmailField(max_length=100, verbose_name='Submitter Email')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    psw_need_qty = PositiveIntegerField(default=0, verbose_name='Quantity Required')
    psw_due_date = models.DateField(verbose_name='Date Needed')
    psw_part_rev = models.CharField(max_length=50, verbose_name='Revision')
    psw_notes = models.TextField(verbose_name='PSW Notes')
