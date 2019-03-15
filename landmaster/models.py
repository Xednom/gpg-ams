import uuid

from django.db import models

from fillables.models import CompanyName


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DueDiligence(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_requested = models.DateField(null=True, blank=True)
    company_name = models.ForeignKey(CompanyName, null=True, blank=True, on_delete=models.PROTECT)
    company_owner = models.CharField(max_length=250, null=True, blank=True)
    date_completed_or_returned = models.DateField(verbose_name='Date Completed or Returned to the Client',
                                                 null=True, blank=True)
    customer_care_specialist = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.company_name)

    class Meta:
        ordering = ['date_requested']

    


class LandData(models.Model):
    owner_name = models.ForeignKey(DueDiligence, null=True, blank=True, on_delete=models.PROTECT)
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

    def __str__(self):
        return str(self.owner_name)


class AdditionalLandInfo(models.Model):
    client_name = models.ForeignKey(DueDiligence, null=True, blank=True, on_delete=models.PROTECT)
    closest_major_city = models.CharField(max_length=250, null=True, blank=True)
    closest_small_town = models.CharField(max_length=250, null=True, blank=True)
    nearby_attractions = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.client_name)


class CountyData(models.Model):
    client_name = models.ForeignKey(DueDiligence, null=True, blank=True, on_delete=models.PROTECT)
    assessor_website = models.URLField(max_length=250, null=True, blank=True)
    treasurer_website = models.URLField(max_length=250, null=True, blank=True)
    recorder_cleark_website = models.URLField(max_length=250, null=True, blank=True)
    zoning_department_website = models.URLField(max_length=250, null=True, blank=True)
    gis_website = models.URLField(max_length=250, null=True, blank=True)
    cad_website = models.URLField(max_length=250, null=True, blank=True)
    planning_department_contact = models.CharField(max_length=250, null=True, blank=True)
    recorder_clerk_contact = models.CharField(max_length=250, null=True, blank=True)
    tax_office_contact = models.CharField(max_length=250, null=True, blank=True)
    assessors_office_contact = models.CharField(max_length=250, null=True, blank=True, verbose_name="Assessor's Office Contact")

    def __str__(self):
        return str(self.client_name)


class TaxData(models.Model):
    client_name = models.ForeignKey(DueDiligence, null=True, blank=True, on_delete=models.PROTECT)
    back_taxes = models.CharField(max_length=250, null=True, blank=True, verbose_name="Back Taxes owed? If so, amount owed.")
    tax_liens = models.CharField(max_length=250, null=True, blank=True, verbose_name="Tax Liens? If so, amount owed.")
    annual_property_taxes = models.CharField(max_length=250, null=True, blank=True)
    is_property_part_of_an_hoa = models.BooleanField()
    how_much_dues = models.CharField(max_length=250, null=True, blank=True, verbose_name="Is so how much are the dues?")

    def __str__(self):
        return str(self.client_name)


class ZoningData(models.Model):
    client_name = models.ForeignKey(DueDiligence, null=True, blank=True, on_delete=models.PROTECT)
    zoning = models.CharField(max_length=250, null=True, blank=True)
    terrian_type = models.CharField(max_length=250, null=True, blank=True)
    property_use_code = models.CharField(max_length=250, null=True, blank=True)
    what_can_be_built = models.TextField(null=True, blank=True, verbose_name="What can be build on the property?")
    time_limit_to_build = models.CharField(max_length=250, null=True, blank=True)
    can_camp = models.BooleanField(max_length=250, null=True, blank=True, verbose_name="Can you camp on the property?")
    notes_on_camping = models.TextField(null=True, blank=True)
    rv_allowed = models.BooleanField(verbose_name="RV's allowed on the property?")
    note_on_rv = models.TextField(verbose_name="Note's on RV's")
    mobile_homes = models.BooleanField(verbose_name="Mobile homes allowed on property?")
    notes_on_mobile_homes = models.TextField(null=True, blank=True)
    is_property_flood_zone_area = models.BooleanField(verbose_name="Is the property in the flood zone area?")

    def __str__(self):
        return str(self.client_name)


class DataOnUtilities(models.Model):
    SEWER_OR_SEPTIC_CHOICES = (
        ('Sewer', 'Sewer'),
        ('Septic', 'Septic'),
    )
    client_name = models.ForeignKey(DueDiligence, null=True, blank=True, on_delete=models.PROTECT)
    water = models.BooleanField(verbose_name="Water?")
    sewer_or_septice = models.CharField(max_length=100, choices=SEWER_OR_SEPTIC_CHOICES, null=True, blank=True)
    power = models.BooleanField(verbose_name='Power(electricity)?')
    gas = models.BooleanField(verbose_name='Gas?')
    waste = models.BooleanField(verbose_name='Waste?')

    def __str__(self):
        return str(self.client_name)    

    class Meta:
        verbose_name = 'Data On Utility'
        verbose_name_plural = 'Data On Utilities'
