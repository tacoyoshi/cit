from django.db import models
from products.models import Product
from stations.models import Station

# Create your models here.

class Part(models.Model):

    PUR = 'P'
    MFG = 'M'
    TYPE_CHOICES = [
        (PUR, 'Purchased'),
        (MFG, 'Manufactured'),
    ]

    ASY = 'ASY'
    CST = 'CST'
    FAB = 'FAB'
    KBN = 'KBN'
    PUR = 'PUR'
    RAW = 'RAW'
    TOO = 'TOO'
    VMI = 'VMI'
    CLASS_CHOICES = [
        (ASY, 'Assembly'),
        (CST, 'Customer Service'),
        (FAB, 'Fabricated Part'),
        (KBN, 'Kanban'),
        (PUR, 'Purchased Part'),
        (RAW, 'Raw Material'),
        (TOO, 'Tooling'),
        (VMI, 'Vendor Managed Inventory'),
    ]

    part_number = models.CharField(max_length=50, unique=True, verbose_name='Part Number')
    part_name = models.CharField(max_length=200, verbose_name='Part Description')
    products = models.ManyToManyField(Product, blank=True, verbose_name='Products')
    part_approved = models.BooleanField(default=False, verbose_name='Approved Type Design')
    stations = models.ManyToManyField(Station, blank=True, verbose_name='Stations')
    part_drawing = models.CharField(max_length=100, blank=True, verbose_name='Parent Document')
    part_qty_per = models.DecimalField(max_digits=8, decimal_places=2, default=1.00, verbose_name='Shipset Qty')
    part_replaces = models.CharField(max_length=50, blank=True, verbose_name='Replaces Part Number')
    part_type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='P', verbose_name='Type')
    part_class = models.CharField(max_length=3, choices=CLASS_CHOICES, default='PUR', verbose_name='Class')
    part_cost = models.DecimalField(max_digits=11, decimal_places=2, default=0.0, verbose_name='Cost')
    part_ium = models.CharField(max_length=2, default='EA', verbose_name='IUM')
    part_pum = models.CharField(max_length=2, default='EA', verbose_name='PUM')
    part_factor = models.PositiveIntegerField(default=1, verbose_name='Conversion Factor')
    part_min_order = models.PositiveIntegerField(default=0, verbose_name='Min Order Quantity')
    part_lead_time = models.PositiveIntegerField(default=0, verbose_name='Lead Time')
    part_rubber = models.BooleanField(default=False, verbose_name='Rubber Like Material')
    part_temp_control = models.BooleanField(default=False, verbose_name='Temperature Controlled')
    part_shelf_life = models.BooleanField(default=False, verbose_name='Shelf Life')
    part_min_stock = models.PositiveIntegerField(default=0, verbose_name='Min On Hand Quantity')
    part_lot_size = models.PositiveIntegerField(default=0, verbose_name='Lot Size')
    part_pln_code = models.CharField(max_length=2, blank=True, verbose_name='Planning Code')
    part_serial_track = models.BooleanField(default=False, verbose_name='Serial Tracked')
    part_lot_track = models.BooleanField(default=False, verbose_name='Lot Tracked')
    part_non_stock = models.BooleanField(default=False, verbose_name='Non-Stock')
    part_qty_bearing = models.BooleanField(default=True, verbose_name='Quantity Bearing')
    part_qasr = models.CharField(max_length=200, blank=True, verbose_name='Quality Requirements')
    part_trace_id = models.BooleanField(default=True, verbose_name='Trace ID Required')

    def __str__(self):
        return  self.part_number

    class Meta:
        ordering = ['part_number']
