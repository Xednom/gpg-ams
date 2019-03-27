import uuid

from django.db import models


class CustomerCareSpecialist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class CygnusInvestment(models.Model):
    PROVIDED_CHOICES = (
        ('YES', 'Yes'),
        ('NO', 'No')
    )
    LISTING_CHOICES = (
        ('LANDWATCH', 'Landwatch'),
        ('LANDPIN', 'Landpin'),
        ('LANDS OF AMERICA', 'Lands of America'),
        ('CRAIGSLIST', 'Craigslist'),
        ('LAND AND FARM', 'Land and Farm'),
        ('KSL', 'KSL'),
        ('ZILLOW', 'Zillow'),
        ('ULTIMATE LAND LISTINGS', 'Ultimate Land Listings'),
        ('LETGO', 'Letgo'),
        ('LANDHUB', 'Landhub'),
        ('LANDMODO', 'LandModo'),
        ('LANDSALELISTING', 'LandSaleListing'),
        ('ADLANDPRO', 'AdLandPro'),
        ('LANDCENTURY', 'LandCentury'),
        ('LANDFLIP', 'LandFlip'),
        ('FACEBOOK', 'Facebook'),
        ('TWITTER', 'Twitter'),
        ('INSTAGRAM', 'Instagram'),
        ('NEIGHBOR LETTER', 'Neighbor Letter'),
        ('EMAIL MARKERTING', 'Email Marketing')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    call_date = models.DateField(null=True, blank=True)
    customer_care_specialist = models.ForeignKey(CustomerCareSpecialist, null=True, blank=True, on_delete=models.PROTECT)
    provided_contact_information = models.CharField(max_length=10, choices=PROVIDED_CHOICES, 
                                                    verbose_name="Have you provided Mr. Temes with your contact information? (if yes, skip questions below, and take brief message) ")
    address_of_property = models.TextField(null=True, blank=True, verbose_name="What is address of the property you are interested in? ")
    name = models.CharField(max_length=250, null=True, blank=True, verbose_name="What is your name?")
    agent = models.CharField(max_length=250, null=True, blank=True, verbose_name="Are you an agent?")
    listing = models.CharField(max_length=250, null=True, blank=True, choices=LISTING_CHOICES, verbose_name="Where did you see the listing?")
    phone_number = models.CharField(max_length=250, null=True, blank=True, verbose_name="What's your phone number?")
    email = models.EmailField(max_length=250, null=True, blank=True, verbose_name="What's your email address?")
    handling_time = models.CharField(max_length=250, null=True, blank=True, verbose_name="Average handling time")
    additional_notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Cygnus Investment Buyer Data"
        verbose_name_plural = "Cygnus Investment Buyer Datas"

    def __str__(self):
        return str(self.name)


class WeBuyAcreageLlc(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    call_date = models.DateField(null=True, blank=True)
    customer_care_specialist = models.ForeignKey(CustomerCareSpecialist, null=True, blank=True, on_delete=models.PROTECT)
    contact_information = models.CharField(max_length=250, null=True, blank=True,
                                           help_text="Have you provided (Jeff) with your contact information? (if yes, skip questions below, and take a brief message)")
    address_or_apn = models.TextField(null=True, blank=True, 
                                           help_text="What is the address of the property you are interested in?(If the caller does NOT have the property address, ask them...)What is the APN number?")
    name_of_the_caller = models.CharField(max_length=250, null=True, blank=True)
    phone_number_of_caller = models.CharField(max_length=250, null=True, blank=True)
    are_you_an_agent = models.CharField(max_length=250, null=True, blank=True)
    listing = models.CharField(max_length=250, null=True, blank=True, help_text="Where did you see the listing?")
    your_phone_number = models.CharField(max_length=250, null=True, blank=True, help_text="What is your Phone number?")
    email_address = models.EmailField(max_length=250, null=True, blank=True, help_text="What is your email address")
    average_handling_time = models.CharField(max_length=250, null=True, blank=True, help_text="Average Handling Time")
    additional_notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "We Buy Acreage LLC Buyer Data"
        verbose_name_plural = "We Buy Acreage LLC Buyer Data"

    def __str__(self):
        return str(self.customer_care_specialist)
