from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


from django.db import models
from django.contrib.auth.models import AbstractUser
# from rest_framework.authtoken.models import Token


class CustomUser(AbstractUser):
    # add additional fields in here
    STATUS = (
        ('REGULAR', 'Regular'),
        ('PROBATIONARY', 'Probationary'),
        ('INACTIVE', 'Inactive'),
    )
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
        verbose_name = 'List of Staff'
        verbose_name = 'List of Staffs'

    def __str__(self):
        return self.full_name


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
#     else:
#         for user in sender.objects.all():
#             Token.objects.get_or_create(user=user)
