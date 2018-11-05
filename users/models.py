from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token


class CustomUser(AbstractUser):
    # add additional fields in here
    STATUS = (
        ('REGULAR', 'Regular'),
        ('PROBATIONARY', 'Probationary'),
        ('INACTIVE', 'Inactive'),
    )
    full_name = models.CharField(max_length=250, default="My Name")
    phone_number = models.CharField(max_length=100)
    SSS_number = models.CharField(max_length=250)
    TIN_number = models.CharField(max_length=250)
    pag_ibig_number = models.CharField(max_length=250)
    philhealth = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    id_number = models.CharField(max_length=250)
    date_of_birth = models.DateField(null=True, blank=True)
    blood_type = models.CharField(max_length=150)
    mother_full_maiden_name = models.CharField(max_length=250)
    father_full_name = models.CharField(max_length=250)
    emergency_contact_name = models.CharField(max_length=250)
    emergency_contact_number = models.CharField(max_length=250)
    relationship_to_the_emergency_contact_person = models.CharField(max_length=200)
    residential_address = models.TextField()
    notes = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.full_name
