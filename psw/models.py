from django.db import models
from parts.models import Part
from projects.models import Project
from django.contrib.auth.models import User

# Create your models here.

NEW = 'NEW'
PEN = 'PEN'
PUR = 'PUR'
SCM = 'SCM'
QUA = 'QUA'
CIT = 'CIT'
ACC = 'ACC'
BUY = 'BUY'
CMP = 'CMP'
HLD = 'HLD'
CAN = 'CAN'

STATUS_CHOICES = [
    (NEW, 'New'),
    (PEN, 'Pending Assignment'),
    (PUR, 'Purchasing'),
    (SCM, 'Supply Chain'),
    (QUA, 'Quality'),
    (CIT, 'CIT'),
    (ACC, 'Accounting'),
    (BUY, 'Pending Purchase'),
    (CMP, 'Complete'),
    (HLD, 'On Hold'),
    (CAN, 'Cancelled'),
]

class Psw(Part):
    psw_number = models.PositiveIntegerField(unique=True, verbose_name='PSW Number', editable=False)
    psw_created = models.DateField(auto_now_add=True, verbose_name='Date Created')
    psw_requestor = models.EmailField(max_length=100, verbose_name='Submitter Email')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, verbose_name='Project')
    psw_need_qty = models.PositiveIntegerField(default=0, blank=True, verbose_name='Quantity Required')
    psw_due_date = models.DateField(blank=True, verbose_name='Date Needed')
    psw_part_rev = models.CharField(max_length=50, blank=True, verbose_name='Revision')
    psw_notes = models.TextField(blank=True, verbose_name='PSW Notes')
    psw_req_min = models.IntegerField(default=0, verbose_name='Requested Min Stock')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='buyers',verbose_name='Buyer')
    supplier_name = models.CharField(max_length=100, blank=True, verbose_name='Supplier Name')
    supplier_id = models.CharField(max_length=8, blank=True, verbose_name='Supplier ID')
    purchase_point = models.CharField(max_length=4, blank=True, verbose_name='Purchase Point')
    supplier_approved = models.BooleanField(default=True, verbose_name='Approved Supplier')
    supplier_part_number = models.CharField(max_length=50, blank=True, verbose_name='Supplier Part Number')
    po_number = models.CharField(max_length=10, blank=True, verbose_name='PO Number')
    po_due_date = models.DateField(blank=True, verbose_name='PO Due Date')
    purchasing_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='purchasing_users',verbose_name='Purchasing User')
    purchasing_date = models.DateField(blank=True, verbose_name='Purchasing Complete')
    scm_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='scm_users',verbose_name='Supply Chain User')
    scm_date = models.DateField(blank=True, verbose_name='Supply Chain Complete')
    quality_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='quality_users',verbose_name='Quality User')
    quality_date = models.DateField(blank=True, verbose_name='Quality Complete')
    cit_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='cit_users',verbose_name='CIT User')
    cit_date = models.DateField(blank=True, verbose_name='CIT Complete')
    accounting_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='accounting_users',verbose_name='Accounting User')
    accounting_date = models.DateField(blank=True, verbose_name='Accounting Complete')
    purchase_date = models.DateField(blank=True, verbose_name='Purchase Date')
    psw_status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='NEW', verbose_name='PSW Status')
    psw_completed = models.DateField(blank=True, verbose_name='Completed Date')

    def __str__(self):
        return  self.psw_number + ' - ' + self.part_number

    class Meta:
        ordering = ['-psw_number']
        get_latest_by = ['psw_number', 'psw_created']
        verbose_name = 'PSW'
        verbose_name_plural = "PSW's"
