from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from decimal import Decimal
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
        ('General Administrative Support', 'General Administrative Support'),
        ('Executive Assistant', 'Executive Assistant'),
        ('Human Resource Specialists', 'Human Resource Specialists')
    )
    CATEGORY = (
        ('Office Based', 'Office Based'),
        ('Part-timers', 'Part-timers'),
        ('Home Based', 'Home Based'),
        ('Freelance', 'Freelance'),
    )
    username = models.OneToOneField(CustomUser, on_delete=models.PROTECT, related_name='staffs')
    full_name = models.CharField(max_length=250, default="My Name")
    middle_name = models.CharField(max_length=150, null=True, blank=True, default="middle name")
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    SSS_number = models.CharField(max_length=250, null=True, blank=True)
    TIN_number = models.CharField(max_length=250, null=True, blank=True)
    pag_ibig_number = models.CharField(max_length=250, null=True, blank=True)
    philhealth = models.CharField(max_length=250, null=True, blank=True, verbose_name="Philhealth Number")
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
    bank_name = models.CharField(max_length=150, null=True, blank=True)
    bank_account_name = models.CharField(max_length=150, null=True, blank=True)
    bank_type = models.CharField(max_length=150, null=True, blank=True)
    bank_account_number = models.CharField(max_length=150, null=True, blank=True)
    base_pay = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True)
    hourly_rate = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True)
    employer_share_sss = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True, verbose_name="Employer share(SSS)")
    employer_share_ec_sss = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True, verbose_name="Employer share EC(SSS)")
    employer_share_philhealth = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True,verbose_name="Employer share(PHILHEALTH)")
    employer_share_pag_ibig = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True, verbose_name="Employer share(PAG-IBIG)")
    total_employer = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True, verbose_name="Total")
    employee_share_sss = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True, verbose_name="Employee share(SSS)")
    employee_share_ec_sss = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True, verbose_name="Employee share EC(SSS)")
    employee_share_philhealth = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True, verbose_name="Employee share(PHILHEALTH)")
    employee_share_pag_ibig = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True, verbose_name="Employee share(PAG-IBIG)")
    employee_tax = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True)
    total_employee = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True, verbose_name="Total")
    total_share_sss = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True)
    total_share_ec_sss = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True)
    total_share_philhealth = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True)
    total_share_pag_ibig = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True)
    overall_total_share = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True)
    actual_date_hired = models.DateField(default=now, null=True, blank=True)
    date_hired_in_contract = models.DateField(default=now, null=True, blank=True)
    category = models.CharField(max_length=150, choices=CATEGORY, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        verbose_name = "List of Staff"
        verbose_name_plural = "List of Staffs"
        ordering = ['full_name']

    def __str__(self):
        return self.full_name

    def compute_total_share(self):
        self.total_share_sss = self.employee_share_sss + self.employer_share_sss
        self.total_share_ec_sss = self.employee_share_ec_sss + self.employer_share_ec_sss
        self.total_share_philhealth = self.employee_share_philhealth + self.employer_share_philhealth
        self.total_share_pag_ibig = self.employee_share_pag_ibig + self.employer_share_pag_ibig
        self.overall_total_share = self.total_share_sss + \
            self.total_share_ec_sss + self.total_share_philhealth + \
            self.total_share_pag_ibig
        total_share = Decimal(self.overall_total_share)
        return total_share

    def save(self, *args, **kwargs):
        self.total_employer = self.employer_share_sss + self.employer_share_ec_sss + self.employer_share_philhealth \
            + self.employer_share_pag_ibig
        self.total_employee = self.employee_share_sss + self.employee_share_ec_sss + self.employee_share_philhealth \
            + self.employee_share_pag_ibig + self.employee_tax
        self.overall_total_share = self.compute_total_share()
        super().save(*args, **kwargs)


class Clients(models.Model):
    COMPANY_CATEGORY = (
        ('landmaster.us', 'landmaster.us'),
        ('gpgcorporations.com', 'gpgcorporations.com'),
        ('callme.com.ph', 'callme.com.ph'),
        ('virtualExpressServices.com', 'virtualExpressServices.com'),
        ('creatif-designs.com', 'creatif-designs.com'),
        ('vacantpropertiesglobal.com', 'vacantpropertiesglobal.com')
    )
    STATUS = (
        ('New', 'New'),
        ('Active', 'Active'),
        ('Inactive within 30 days', 'Inactive within 30 days'),
        ('Inactive within 90 days', 'Inactive within 90 days'),
        ('Inactive within 120 days', 'Inactive within 120 days'),
        ('Sign out', 'Sign out'),
        ('Terminated', 'Terminated'),
        ('Others', 'Others')
    )
    username = models.OneToOneField(CustomUser, on_delete=models.PROTECT, related_name='clients')
    full_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    date_signed_up = models.DateTimeField(default=now, null=True, blank=True)
    client_control_number = models.CharField(max_length=150, null=True, blank=True)
    referred_by = models.CharField(max_length=150, null=True, blank=True)
    lead_source = models.CharField(max_length=150, null=True, blank=True)
    assigned_va = models.ForeignKey(VirtualAssistant, null=True, blank=True, verbose_name="Assigned VA", on_delete=models.PROTECT)
    assigned_pm = models.ForeignKey(ProjectManager, null=True, blank=True, verbose_name="Assigned PM", on_delete=models.PROTECT)
    task_enroute = models.CharField(max_length=150, null=True, blank=True)
    type_of_task = models.TextField(null=True, blank=True)
    internal_folder_link_1 = models.URLField(null=True, blank=True)
    internal_folder_link_2 = models.URLField(null=True, blank=True)
    internal_folder_link_3 = models.URLField(null=True, blank=True)
    phone_number = models.CharField(max_length=150, null=True, blank=True)
    company_category = models.CharField(max_length=150, choices=COMPANY_CATEGORY, null=True, blank=True)
    status = models.CharField(max_length=150, choices=STATUS, null=True, blank=True, default='New')

    class Meta:
        verbose_name = 'List of Client'
        verbose_name_plural = 'List of Clients'

    def __str__(self):
        return self.full_name


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
	print('user profile created', created)
	if instance.is_staffs:
		Staffs.objects.get_or_create(username=instance)
	elif instance.is_client:
		Clients.objects.get_or_create(username=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
	print('user profile saved')
	# print(instance.internprofile.bio, instance.internprofile.location)
	if instance.is_staffs:
		    instance.staffs.save()
	elif instance.is_client:
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

    def __str__(self):
        return self.url


class TypeOfTaskRequest(models.Model):
    name = models.ForeignKey(Clients, on_delete=models.PROTECT, null=True, blank=True)
    name_of_task = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name_of_task


class ChannelOfCommunications(models.Model):
    name = models.ForeignKey(Clients, on_delete=models.PROTECT, null=True, blank=True)
    name_of_channel = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = "Channel of Communication"
        verbose_name_plural = "Channel of Communications"
    
    def __str__(self):
        return self.name_of_channel


class NotesAfterTraining(models.Model):
    name = models.ForeignKey(Clients, on_delete=models.PROTECT, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.notes
