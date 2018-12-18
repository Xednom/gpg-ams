import uuid
import datetime
from django.db import models


class CareSpecialistReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name_appeared_from_letter = models.CharField(max_length=250, verbose_name='Company name or Name appread from Letter received')
    care_specialist = models.CharField(max_length=250, null=True, blank=True)
    date_of_the_lead_called = models.DateField(null=True, blank=True)
    full_name_of_the_caller = models.CharField(max_length=250, null=True, blank=True)
    caller_id = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=250, null=True, blank=True)
    receive_letter = models.CharField(max_length=100, null=True, blank=True, verbose_name='Did you receive a letter from us?(IF YES, PROCEED TO THE NEXT QUESTION)')
    notes = models.TextField(null=True, blank=True, verbose_name='IF NO, DO NOT PROCEED AND JUST ASK THE CONCERN OF THE CALLER')
    property_located = models.CharField(max_length=250, null=True, blank=True, verbose_name='Where is the property located? Please specify the county & state?')
    apn_property_id = models.CharField(max_length=250, null=True, blank=True, verbose_name='What is the property APN/property ID, including the dashes?')
    selling_property = models.CharField(max_length=250, null=True, blank=True, verbose_name='Are you interested in selling this property? (If yes, continue with script. If NO ask the question below)')
    price_looking_to_get_property = models.CharField(max_length=250, null=True, blank=True, verbose_name=' What price are you looking to get for the property?')
    owner_of_the_property = models.CharField(max_length=250, null=True, blank=True, verbose_name="Are you the owner of the property as per county's record? If No: Ask the question below.")
    name_on_the_record = models.TextField(null=True, blank=True, verbose_name='May I ask whose name is on reord with the county?')
    mailed_from = models.CharField(max_length=100, null=True, blank=True, verbose_name='Is the address we mailed from letter we sent is correct? If no: please ask the question below.')
    mailing_address = models.TextField(null=True, blank=True, verbose_name='What is your mailing address?')
    contact_number = models.TextField(null=True, blank=True, verbose_name='Is this the best ccontact number that we can reach you? (Please verify phone number with the caller - read back to them)')
    email_address = models.EmailField(null=True, blank=True, verbose_name='May I have your emaill address?')
    properties = models.CharField(max_length=250, null=True, blank=True, verbose_name='Do you own one or several properties you would like to sell? If several: please ask the question below.')
    apn_counties = models.TextField(null=True, blank=True, verbose_name="Please gather all the APN's and counties of the properties they would like to sell.")
    taxes = models.CharField(max_length=250, null=True, blank=True, verbose_name='Are the  taxes up to date or paid?If not up to date please ask for the current total amount due')
    total_current_amount_due = models.TextField(null=True, blank=True, verbose_name='Total Current Amount Due?')
    special_attribute = models.TextField(null=True, blank=True, verbose_name='Any special attibutes of the property? Water well, near power pole or treed, easy road access, etc)')
    info_on_the_property = models.TextField(null=True, blank=True, verbose_name='Is there anything else you would like to tell us about this property?')
    extra_comments = models.TextField(null=True, blank=True, verbose_name='Notes if caller says extra comments:')
    email_sent_to_the_owner = models.CharField(max_length=250, null=True, blank=True, verbose_name='Eamil sent to the Owner?')
    calendar_invite = models.CharField(max_length=250, null=True, blank=True, verbose_name='Calendar Invite Sent to the Owner? ( In case of Hot Leads)')
    total_minutes_answered = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Total Minutes Answered')

    class Meta:
        ordering = ['-name_appeared_from_letter']

    def __str__(self):
        return self.care_specialist
