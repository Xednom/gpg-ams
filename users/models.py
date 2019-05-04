from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

from fillables.models import VirtualAssistant, ProjectManager


class CustomUser(AbstractUser):
    # add additional fields in here for custom user
    notes = models.TextField(null=True, blank=True)
    is_staffs = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

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
    JOB_POSITION = (
        ('Senior Operations Managers', 'Senior Operations Managers'),
        ('Project Managers', 'Project Managers'),
        ('Team Leads', 'Team Leads'),
        ('General Administrative Support', 'General Administrative Support')
    )
    username = models.OneToOneField(CustomUser, on_delete=models.PROTECT, related_name='staffs')
    full_name = models.CharField(max_length=250, default="My Name")
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    SSS_number = models.CharField(max_length=250, null=True, blank=True)
    TIN_number = models.CharField(max_length=250, null=True, blank=True)
    pag_ibig_number = models.CharField(max_length=250, null=True, blank=True)
    philhealth = models.CharField(max_length=250, null=True, blank=True)
    position = models.CharField(max_length=150, choices=JOB_POSITION, null=True, blank=True)
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
    bank_name = models.CharField(max_length=150)
    bank_account_name = models.CharField(max_length=150)
    bank_type = models.CharField(max_length=150)
    bank_account_number = models.CharField(max_length=150)

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
    date_signed_up = models.DateTimeField(default=now, null=True, blank=True)
    client_control_number = models.CharField(max_length=150, null=True, blank=True)
    referral = models.CharField(max_length=150, null=True, blank=True)
    assigned_va = models.ForeignKey(VirtualAssistant, null=True, blank=True, on_delete=models.PROTECT)
    assigned_pm = models.ForeignKey(ProjectManager, null=True, blank=True, on_delete=models.PROTECT)
    task_enroute = models.CharField(max_length=150, null=True, blank=True)
    type_of_task = models.TextField(null=True, blank=True)
    internal_folder_link = models.URLField(null=True, blank=True)


    class Meta:
        verbose_name = 'List of Client'
        verbose_name_plural = 'List of Clients'

    def __str__(self):
        return self.full_name


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
	print('****', created)
	if instance.is_staffs:
		Staffs.objects.get_or_create(username=instance)
	else:
		Clients.objects.get_or_create(username=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
	print('_-----')
	# print(instance.internprofile.bio, instance.internprofile.location)
	if instance.is_staffs:
		    instance.staffs.save()
	else:
            Clients.objects.get_or_create(username=instance)


class ClientProfiling(models.Model):
    kind_of_client = models.CharField(max_length=150)
    client_name = models.ForeignKey(Clients, null=True, blank=True, on_delete=models.PROTECT)
    notes = models.TextField()
    
    class Meta:
        verbose_name = 'Client Profile'
        verbose_name_plural = 'Client Profiles'
        ordering = ['kind_of_client']


class Email(models.Model):
    name = models.ForeignKey(Clients, on_delete=models.PROTECT, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.email_address


class PaypalEmail(models.Model):
    name = models.ForeignKey(Clients, on_delete=models.PROTECT, null=True, blank=True)
    paypal_email_address = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.paypal_email_address


class WebsiteUrl(models.Model):
    name = models.ForeignKey(Clients, on_delete=models.PROTECT, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.url


class TrainingUrl(models.Model):
    name = models.ForeignKey(Clients, on_delete=models.PROTECT, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
