from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # add additional fields in here for custom user
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'List of Username'
        verbose_name_plural = 'List of Usernames'
        ordering = ['notes']

    def __str__(self):
        return self.username

class Staffs(models.Model):
    STATUS = (
        ('REGULAR', 'Regular'),
        ('PROBATIONARY', 'Probationary'),
        ('INACTIVE', 'Inactive'),
    )
    user_name = models.OneToOneField(CustomUser, on_delete=models.PROTECT, related_name='staffs')
    full_name = models.CharField(max_length=250, default="My Name")
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    SSS_number = models.CharField(max_length=250, null=True, blank=True)
    TIN_number = models.CharField(max_length=250, null=True, blank=True)
    pag_ibig_number = models.CharField(max_length=250, null=True, blank=True)
    philhealth = models.CharField(max_length=250, null=True, blank=True)
    position = models.CharField(max_length=250, null=True, blank=True)
    id_number = models.CharField(max_length=250, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    blood_type = models.CharField(max_length=150, null=True, blank=True)
    mother_full_maiden_name = models.CharField(max_length=250, null=True, blank=True)
    father_full_name = models.CharField(max_length=250, null=True, blank=True)
    emergency_contact_name = models.CharField(max_length=250, null=True, blank=True)
    emergency_contact_number = models.CharField(max_length=250, null=True, blank=True)
    relationship_to_the_emergency_contact_person = models.CharField(max_length=200, null=True, blank=True)
    residential_address = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, null=True, blank=True)

    class Meta:
        verbose_name = "List of Staff"
        verbose_name_plural = "List of Staffs"
        ordering = ['full_name']

    def __str__(self):
        return self.full_name


class Clients(models.Model):
    username = models.OneToOneField(CustomUser, on_delete=models.PROTECT, related_name='clients')
    full_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'List of Client'
        verbose_name_plural = 'List of Clients'

    def __str__(self):
        return self.full_name
