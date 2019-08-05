import uuid

from django.db import models
from django.utils.timezone import now


class Inventory(models.Model):
    SITES = (
        ('LandModo', 'LandModo'),
        ('Zillow', 'Zillow'),
        ('Craigslist', 'Craigslist'),
        ('Facebook MarketPlace', 'Facebook MarketPlace'),
        ('KSL.com', 'KSL.com'),
        ('Ultimate Land Listings', 'Ultimate Land Listings'),
        ('LandCentury', 'LandCentury'),
        ('Landhub', 'Landhub'),
        ('Lands of America', 'Lands of America'),
        ('Landpin', 'Landpin'),
        ('Landwatch', 'Landwatch'),
        ('Landflip', 'Landflip'),
        ('Others', 'Others'),
    )
    APPROVAL = (
        ('Approved', 'Approved'),
        ('Pending for Approval', 'Pending for Approval'),
    )
    STATUS = (
        ('In progress', 'In progress'),
        ('Complete', 'Complete')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_requested = models.DateField(default=now, null=True, blank=True)
    date_completed = models.DateField(default=now, null=True, blank=True)
    type_of_marketing_sites = models.CharField(max_length=150, choices=SITES, null=True, blank=True)
    indicate_others = models.CharField(max_length=150, null=True, blank=True)
    client_full_name = models.CharField(max_length=150, null=True, blank=True)
    client_company_name = models.CharField(max_length=150, null=True, blank=True)
    apn = models.TextField(null=True, blank=True)
    title_of_the_post = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=150, null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    url_link = models.TextField(null=True, blank=True)
    marketing_associate = models.CharField(max_length=150, null=True, blank=True)
    duration = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    post_for_approval = models.CharField(max_length=150, choices=APPROVAL, null=True, blank=True)
    status = models.CharField(max_length=150, choices=STATUS, default=[0][0], null=True, blank=True)
    additional_notes = models.TextField(null=True, blank=True)
    notes_from_the_client = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Marketing Sites Inventory'
        verbose_name_plural = 'Marketing Sites Inventories'
        ordering = ['-date_requested']

    def __str__(self):
        return self.client_full_name
