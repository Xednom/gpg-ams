import uuid

from decimal import Decimal
from django.db import models
from django.conf import settings

from django.utils.timezone import now
from django.urls import reverse

from fillables.models import CompanyName, VirtualAssistant
from users.models import Staffs

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
    URGENCY = (
        ('High', 'High'),
        ('Average', 'Average'),
        ('Low', 'Low'),
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
    county_operator_details = models.CharField(max_length=250, null=True, blank=True, help_text="County Operator's Details")
    owner_name = models.CharField(max_length=250, null=True, blank=True, verbose_name="Owner's name")
    parcel_number = models.CharField(max_length=250, null=True, blank=True)
    account_number = models.CharField(max_length=259, null=True, blank=True)
    property_address = models.TextField(null=True, blank=True)
    county = models.CharField(max_length=250, null=True, blank=True)
    lot_number = models.CharField(max_length=250, null=True, blank=True)
    legal_description = models.TextField(null=True, blank=True)
    parcel_size = models.CharField(max_length=250, null=True, blank=True)
    gps_coordinates = models.CharField(max_length=250, null=True, blank=True, verbose_name="GPS Coordinates")
    gps_coordinates_4_corners = models.CharField(max_length=250, null=True, blank=True, verbose_name="GPS Coordinates 4 Corners")
    google_map_link = models.URLField(max_length=250, null=True, blank=True)
    elevation = models.CharField(max_length=250, null=True, blank=True)
    assessed_value = models.CharField(max_length=250, null=True, blank=True)
    closest_major_city = models.CharField(max_length=250, null=True, blank=True)
    closest_small_town = models.CharField(max_length=250, null=True, blank=True)
    nearby_attractions = models.CharField(max_length=250, null=True, blank=True, verbose_name="Nearby Attractions and Amenities")
    assessor_website = models.URLField(max_length=250, null=True, blank=True)
    treasurer_website = models.URLField(max_length=250, null=True, blank=True)
    recorder_clerk_website = models.URLField(max_length=250, null=True, blank=True, verbose_name="Recorder/Clerk Website")
    zoning_department_website = models.URLField(max_length=250, null=True, blank=True)
    gis_website = models.URLField(max_length=250, null=True, blank=True, verbose_name="GIS Website")
    cad_website = models.URLField(max_length=250, null=True, blank=True, verbose_name="CAD Website")
    planning_department_contact = models.CharField(max_length=250, null=True, blank=True)
    recorder_clerk_contact = models.CharField(max_length=250, null=True, blank=True)
    tax_office_contact = models.CharField(max_length=250, null=True, blank=True)
    assessors_office_contact = models.CharField(max_length=250, null=True, blank=True, verbose_name="Assessor's Office Contact")
    utility_department_number = models.CharField(max_length=150, null=True, blank=True)
    water_company_number= models.CharField(max_length=150, null=True, blank=True)
    electricity_company_number = models.CharField(max_length=150, null=True, blank=True)
    propane_gas_company_number = models.CharField(max_length=150, null=True, blank=True)
    natural_gas_company_number = models.CharField(max_length=150, null=True, blank=True)
    back_taxes = models.CharField(max_length=250, null=True, blank=True, verbose_name="Back Taxes owed?",
                                  help_text="Is there any back Taxes owed in the property? If yes, how much is the amount owed...")
    tax_liens = models.CharField(max_length=250, null=True, blank=True, verbose_name="Tax Liens?",
                                 help_text="Is there any Tax Liens? If yes, how much is the amount owed...")
    annual_property_taxes = models.CharField(max_length=250, null=True, blank=True, help_text="What is the Annual Property Tax?")
    is_property_part_of_an_hoa = models.CharField(max_length=250, null=True, blank=True, help_text="Is the property part of an HOA?")
    how_much_dues = models.CharField(max_length=250, null=True, blank=True,
                                     verbose_name="how much are the dues?", help_text="If yes, how much being the dues?")
    zoning = models.CharField(max_length=250, null=True, blank=True,
                              help_text="What is the zoning of the property?")
    terrian_type = models.CharField(max_length=250, null=True, blank=True, help_text="Is it flat or slope? etc.")
    property_use_code = models.CharField(max_length=250, null=True, blank=True)
    what_can_be_built = models.TextField(null=True, blank=True, verbose_name="What can be build on the property?",
                                         help_text="What can be built on the property? Indicate different types of homes that we can build on the lots.")
    time_limit_to_build = models.CharField(max_length=250, null=True, blank=True, help_text="Is there any time limit to build?")
    can_camp = models.CharField(max_length=250, null=True, blank=True, verbose_name="Can you camp on the property?",
                                help_text="If we buy this property can the owner camp there?")
    notes_on_camping = models.TextField(null=True, blank=True, help_text="Notes on Camping?")
    rv_allowed = models.CharField(max_length=250, null=True, blank=True, verbose_name="RV's allowed on the property?",
                                  help_text="Is RV's allowed on the property? Please ask if there are restrictions.")
    note_on_rv = models.TextField(null=True, blank=True, verbose_name="Note's on RV's")
    mobile_homes = models.CharField(max_length=250, null=True, blank=True, verbose_name="Mobile homes allowed on property?",
                                    help_text="Are mobile homes allowed on the property? Please ask if there is restrictions.")
    notes_on_mobile_homes = models.TextField(null=True, blank=True, help_text="Notes on mobile homes?")
    is_property_flood_zone_area = models.CharField(max_length=250, null=True, blank=True, verbose_name="Flood zone area?", help_text="Is the property in a flood zone area?")
    access_to_property = models.CharField(max_length=250, null=True, blank=True, verbose_name='Access to Property', help_text="Dirt / Paved or No Access")
    water = models.CharField(max_length=250, null=True, blank=True, verbose_name="Water?")
    sewer_or_septic = models.CharField(max_length=100, choices=SEWER_OR_SEPTIC_CHOICES, null=True, blank=True)
    power = models.CharField(max_length=250, null=True, blank=True, verbose_name='Power(electricity)?')
    gas = models.CharField(max_length=250, verbose_name='Gas?', null=True, blank=True)
    waste = models.CharField(max_length=250, verbose_name='Waste?', null=True, blank=True)
    notes_from_the_client = models.TextField(null=True, blank=True, verbose_name="Client instructions")
    notes_from_the_quality_specialist = models.TextField(null=True, blank=True, verbose_name="Quality Specialists Evaluation")
    notes_from_the_virtual_assistant = models.TextField(null=True, blank=True, verbose_name="VA Notes")
    notes_on_zoning = models.TextField(null=True, blank=True, verbose_name="Zoning Memo")
    notes_on_utilities = models.TextField(null=True, blank=True, verbose_name="Utilities Memo") 
    notes_on_tax = models.TextField(null=True, blank=True, verbose_name="Tax Memo")
    dd_va_assigned_initial_data = models.ForeignKey(settings.STAFFS, null=True, blank=True, on_delete=models.PROTECT,
                                            verbose_name="VA - Initial Data", related_name="initial")
    dd_va_assigned_call_outs_tax_data = models.ForeignKey(settings.STAFFS, null=True, blank=True, on_delete=models.PROTECT,
                                            verbose_name="VA - Tax Data", related_name='tax')
    dd_va_assigned_call_outs_zoning_data = models.ForeignKey(settings.STAFFS, null=True, blank=True, on_delete=models.PROTECT,
                                            verbose_name="VA - Zoning Data", related_name='zoning')
    dd_va_assigned_call_outs_utilities_data = models.ForeignKey(settings.STAFFS, null=True, blank=True, on_delete=models.PROTECT,
                                            verbose_name="VA - Utilities Data", related_name='utilities')
    dd_va_assigned_call_outs_other_requests = models.ForeignKey(settings.STAFFS, null=True, blank=True, on_delete=models.PROTECT,
                                        verbose_name="VA - Other Requests", related_name='other')
    project_manager = models.ForeignKey(Staffs, null=True, blank=True, on_delete=models.PROTECT)
    total_minutes_hours_duration = models.CharField(max_length=150, null=True, blank=True, verbose_name="Total Minutes/hours duration")
    attachments = models.URLField(null=True, blank=True)
    initial_due_diligence_completion = models.DateField(null=True, blank=True, verbose_name="Date of Completion – Initial Data")
    tax_data_completion = models.DateField(null=True, blank=True, verbose_name="Date of Completion – Tax Data")
    zoning_data_completion = models.DateField(null=True, blank=True, verbose_name="Date of Completion – Zoning Data")
    utilities_data_completion = models.DateField(null=True, blank=True, verbose_name="Date of Completion – Utilities Data")
    other_requests_completion = models.DateField(null=True, blank=True, verbose_name="Date of Completion – Other Requests")
    date_of_completion = models.DateField(null=True, blank=True, help_text="Date of Completion Submitted to the Client- Overall Due Diligence")
    operator_details_tax_data = models.TextField(null=True, blank=True, verbose_name="County Operator Details - Tax Data")
    operator_details_zoning_data = models.TextField(null=True, blank=True, verbose_name="County Operator Details - Zoning Data")
    operator_details_utilities_data = models.TextField(null=True, blank=True, verbose_name="County Operator Details - Utilities Data")
    operator_details_other_requests = models.TextField(null=True, blank=True, verbose_name="County Operator Details - Other Requests")
    status_initial_data = models.CharField(max_length=150, choices=STATUS, null=True, blank=True, verbose_name="Due Diligence Status for Initial Data")
    status_tax_data = models.CharField(max_length=150, choices=STATUS, null=True, blank=True, verbose_name="Due Diligence Status for Tax Data")
    status_zoning_data = models.CharField(max_length=150, choices=STATUS, null=True, blank=True, verbose_name="Due Diligence Status for Zoning Data")
    status_utilities_data = models.CharField(max_length=150, choices=STATUS, null=True, blank=True, verbose_name="Due Diligence Status for Utilities Data")
    status_other_requests = models.CharField(max_length=150, choices=STATUS, null=True, blank=True, verbose_name="Due Diligence Status for Other Requests")
    status_of_dd = models.CharField(max_length=150, choices=STATUS, null=True, blank=True, verbose_name="Due Diligence Status")
    level_of_urgency = models.CharField(max_length=150, choices=URGENCY, null=True, blank=True)
    additional_client_request_question = models.TextField(null=True, blank=True,
                                                          verbose_name='Additional Client Request Question/s')
    additional_client_request_memo = models.TextField(null=True, blank=True, 
                                                      verbose_name='Additional Client Request Memo from Cust. Rep')
    total_hrs_for_initial_dd = models.DecimalField(max_digits=7, decimal_places=2,
                                                   default=0.00, null=True, blank=True)
    total_hrs_overall_dd_callouts = models.DecimalField(max_digits=7, decimal_places=2,
                                                        default=0.00, null=True, blank=True)
    total_time_allocation = models.DecimalField(max_digits=7, decimal_places=2,
                                                default=0.00, null=True, blank=True)

    class Meta:
        ordering = ('date_requested',)

    def __str__(self):
        return str(self.company_name)

    def time_calculation(self):
        total = self.total_hrs_for_initial_dd + self.total_hrs_overall_dd_callouts
        overall = Decimal(total)
        return overall
    
    def save(self, *args, **kwargs):
        self.total_time_allocation = self.time_calculation()
        return super().save(*args, **kwargs)


class DueDiligencesCleared(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_of_call = models.DateField(default=now, null=True, blank=True)
    client_full_name = models.ForeignKey(settings.CLIENTS, null=True, blank=True,
                                         on_delete=models.PROTECT)
    apn = models.TextField(null=True, blank=True)
    total_minutes = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    call_details = models.TextField(null=True, blank=True)
    department_calling_about = models.TextField(null=True, blank=True)
    contact_details = models.TextField(null=True, blank=True)
    operator_details = models.TextField(null=True, blank=True)
    additional_memo = models.TextField(null=True, blank=True)
    customer_service_representative = models.ForeignKey(settings.STAFFS, null=True, 
                                                        blank=True, on_delete=models.PROTECT)
    customer_representative_note = models.TextField(null=True, blank=True)
    reason_of_the_call = models.TextField(null=True, blank=True, verbose_name='Reason(s) of the call')
    questions_requested_to_ask = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Due Diligence Call Out Report'
        verbose_name_plural = 'Due Diligence Call Out Reports'
        ordering=['-date_of_call']

    def get_absolute_url(self):
        return reverse('')

    def __str__(self):
        return str(self.client_full_name)
