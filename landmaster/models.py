import uuid

from decimal import Decimal
from django.db import models

from fillables.models import CompanyName, VirtualAssistant, ProjectManager
from django.utils.timezone import now


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DueDiligence(TimeStampedModel):
    SEWER_OR_SEPTIC_CHOICES = (
        ('Sewer', 'Sewer'),
        ('Septic', 'Septic'),
    )
    STATUS = (
        ('Sent to Project Manager', 'Sent to Project Manager'),
        ('Project Managers Review', 'Project Managers Review'),
        ('Sent to VA', 'Sent to VA'),
        ('VA Processing', 'VA Processing'),
        ('Sent to Quality Specialist', 'Sent to Quality Specialist'),
        ('Quality Specialist Checking', 'Quality Specialist Checking'),
        ('Submitted to the Client', 'Submitted to the Client'),
        ('Approved by the Client', 'Approved by the Client'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_requested = models.DateField(null=True, blank=True)
    company_name = models.CharField(max_length=250, null=True, blank=True)
    company_owner_or_requestor = models.CharField(max_length=250, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    customer_care_specialist = models.CharField(
        max_length=250, null=True, blank=True, help_text="Customer Care Specialist or Operator ID, Assessors/County")
    owner_name = models.CharField(max_length=250, null=True, blank=True, verbose_name="Owner's name")
    parcel_number = models.CharField(max_length=250, null=True, blank=True)
    account_number = models.CharField(max_length=259, null=True, blank=True)
    property_address = models.TextField(null=True, blank=True)
    county = models.CharField(max_length=250, null=True, blank=True)
    lot_number = models.CharField(max_length=250, null=True, blank=True)
    legal_description = models.TextField(null=True, blank=True)
    parcel_size = models.CharField(max_length=250, null=True, blank=True)
    gps_coordinates = models.CharField(max_length=250, null=True, blank=True)
    gps_coordinates_4_corners = models.CharField(max_length=250, null=True, blank=True)
    google_map_link = models.URLField(max_length=250, null=True, blank=True)
    elevation = models.CharField(max_length=250, null=True, blank=True)
    assessed_value = models.CharField(max_length=250, null=True, blank=True)
    access_to_property = models.CharField(max_length=250, null=True, blank=True, verbose_name='Access to Property (Dirt or Paved)')
    closest_major_city = models.CharField(max_length=250, null=True, blank=True)
    closest_small_town = models.CharField(max_length=250, null=True, blank=True)
    nearby_attractions = models.CharField(max_length=250, null=True, blank=True)
    assessor_website = models.URLField(max_length=250, null=True, blank=True)
    treasurer_website = models.URLField(max_length=250, null=True, blank=True)
    recorder_clerk_website = models.URLField(max_length=250, null=True, blank=True, verbose_name="Recorder/Clerk Website")
    zoning_department_website = models.URLField(max_length=250, null=True, blank=True)
    gis_website = models.URLField(max_length=250, null=True, blank=True)
    cad_website = models.URLField(max_length=250, null=True, blank=True)
    planning_department_contact = models.CharField(max_length=250, null=True, blank=True)
    recorder_clerk_contact = models.CharField(max_length=250, null=True, blank=True)
    tax_office_contact = models.CharField(max_length=250, null=True, blank=True)
    assessors_office_contact = models.CharField(max_length=250, null=True, blank=True, verbose_name="Assessor's Office Contact")
    back_taxes = models.CharField(max_length=250, null=True, blank=True, verbose_name="Back Taxes owed? If so, amount owed.")
    tax_liens = models.CharField(max_length=250, null=True, blank=True, verbose_name="Tax Liens? If so, amount owed.")
    annual_property_taxes = models.CharField(max_length=250, null=True, blank=True)
    is_property_part_of_an_hoa = models.CharField(max_length=250, null=True, blank=True)
    how_much_dues = models.CharField(max_length=250, null=True, blank=True, verbose_name="Is so how much are the dues?")
    zoning = models.CharField(max_length=250, null=True, blank=True)
    terrian_type = models.CharField(max_length=250, null=True, blank=True)
    property_use_code = models.CharField(max_length=250, null=True, blank=True)
    what_can_be_built = models.TextField(null=True, blank=True, verbose_name="What can be build on the property?")
    time_limit_to_build = models.CharField(max_length=250, null=True, blank=True)
    can_camp = models.CharField(max_length=250, null=True, blank=True, verbose_name="Can you camp on the property?")
    notes_on_camping = models.TextField(null=True, blank=True)
    rv_allowed = models.CharField(max_length=250, null=True, blank=True, verbose_name="RV's allowed on the property?")
    note_on_rv = models.TextField(null=True, blank=True, verbose_name="Note's on RV's")
    mobile_homes = models.CharField(max_length=250, null=True, blank=True, verbose_name="Mobile homes allowed on property?")
    notes_on_mobile_homes = models.TextField(null=True, blank=True)
    is_property_flood_zone_area = models.CharField(max_length=250, null=True, blank=True, verbose_name="Is the property in the flood zone area?")
    water = models.CharField(max_length=250, null=True, blank=True, verbose_name="Water?")
    sewer_or_septic = models.CharField(max_length=100, choices=SEWER_OR_SEPTIC_CHOICES, null=True, blank=True)
    power = models.CharField(max_length=250, null=True, blank=True, verbose_name='Power(electricity)?')
    gas = models.CharField(max_length=250, verbose_name='Gas?', null=True, blank=True)
    waste = models.CharField(max_length=250, verbose_name='Waste?', null=True, blank=True)
    date_completed = models.DateField(null=True, blank=True)
    notes_from_the_client = models.TextField(null=True, blank=True)
    notes_from_the_quality_specialist = models.TextField(null=True, blank=True)
    notes_from_the_virtual_assistant = models.TextField(null=True, blank=True)
    dd_team_assigned_va = models.ForeignKey(VirtualAssistant, null=True, blank=True, on_delete=models.PROTECT,
                                            verbose_name="DD Team Assigned VA")
    project_manager = models.ForeignKey(ProjectManager, null=True, blank=True, on_delete=models.PROTECT)
    total_minutes_hours_duration = models.CharField(max_length=150, null=True, blank=True, verbose_name="Total Minutes/hours duration")
    attachments = models.URLField(null=True, blank=True)
    status_of_dd = models.CharField(max_length=150, choices=STATUS, null=True, blank=True)

    class Meta:
        ordering = ('date_requested',)

    def __str__(self):
        return str(self.company_name)


class DueDiligencesCleared(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_of_call = models.DateField(default=now, null=True, blank=True)
    client_full_name = models.CharField(max_length=150, null=True, blank=True)
    client_company_name = models.CharField(max_length=150, null=True, blank=True)
    apn = models.CharField(max_length=150, null=True, blank=True)
    call_in = models.DateTimeField(null=True, blank=True)
    call_out = models.DateTimeField(null=True, blank=True)
    total_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    department_calling_about = models.CharField(max_length=150, null=True, blank=True)
    contact_number = models.CharField(max_length=150, null=True, blank=True)
    operators_details = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    customer_service_representative = models.ForeignKey(VirtualAssistant, null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Due Diligences Cleared Information'
        verbose_name_plural = 'Due Diligences Cleared Informations'
        ordering=['-date_of_call']

    def calculate_total_hours(self):
        worked_hours = (self.call_out - self.call_in).total_seconds() / 60 / 60
        total_hours = Decimal(worked_hours)
        return total_hours

    def save(self, *args, **kwargs):
        self.total_hours = self.calculate_total_hours()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.client_full_name + " of " + self.client_company_name