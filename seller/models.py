import uuid
import datetime

from django.db import models

from buyer.models import CustomerCareSpecialist


class CygnusInvestmentSeller(models.Model):
    PROVIDED_CHOICES = (
        ('YES', 'Yes'),
        ('NO', 'No')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    call_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    customer_care_specialist = models.ForeignKey(CustomerCareSpecialist, null=True, blank=True, on_delete=models.PROTECT)
    provided_contact_information = models.CharField(max_length=10, choices=PROVIDED_CHOICES, 
                                                    help_text="Have you provided Mr. Temes with your contact information? (if yes, skip questions below, and take brief message)")
    number_printed = models.CharField(max_length=250, null=True, blank=True,
                                      help_text="What is the number printed in the lower right side of the letter you received?")
    name = models.CharField(max_length=250, null=True, blank=True, help_text="What is your name?")
    property_owner = models.CharField(max_length=250, null=True, blank=True, 
                                      help_text="Are you the property owner listed on the deed?")
    other_owners = models.CharField(max_length=250, null=True, blank=True, 
                                    help_text="Are there any other owners listed on the deed?")
    phone_number = models.CharField(max_length=250, null=True, blank=True, help_text="What is your Phone Number?")
    email_address = models.CharField(max_length=250, null=True, blank=True, help_text="What is your email address?")
    average_handling_time = models.FloatField(null=True, blank=True, default=0.00)
    additional_notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Cygnus Investment Seller Data"
        verbose_name_plural = "Cygnus Investment Seller Datas"

    def __str__(self):
        return str(self.customer_care_specialist)

    
class DreamWeaverProperty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    call_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    customer_care_specialist = models.ForeignKey(CustomerCareSpecialist, null=True, blank=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=250, null=True, blank=True, help_text="What is your name?")
    reference_number_or_parcel_number = models.CharField(max_length=250, null=True, blank=True, 
                                                            help_text="Do you have the or Reference # or Parcel number?")
    state_and_county = models.CharField(max_length=250, null=True, blank=True, help_text="State and County?")
    owner_of_the_land = models.CharField(max_length=250, null=True, blank=True, help_text="Are you the Owner of the Land?")
    price = models.CharField(max_length=250, null=True, blank=True,
                                help_text="Do you accept this price? (Yes) Great then we will have purchasing manager call you")
    price_to_sell = models.CharField(max_length=250, null=True, blank=True, 
                                        help_text="IF (NO), What price would you sell this for?")
    phone_number = models.CharField(max_length=100, null=True, blank=True, help_text="What is your Phone number?")
    email_address = models.EmailField(null=True, blank=True)
    average_handling_time = models.FloatField(null=True, blank=True, default=0.00)
    additional_notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Dream Weaver Property Seller Data"
        verbose_name_plural = "Dream Weaver Property Seller Datas"
        
    def __str__(self):
        return str(self.customer_care_specialist)


class OfficeFlowersValleyProperties(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    call_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    customer_care_specialist = models.ForeignKey(CustomerCareSpecialist, null=True, blank=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=250, null=True, blank=True, help_text="Caller's Name")
    phone_number = models.CharField(max_length=250, null=True, blank=True)
    interested_in_selling = models.CharField(max_length=250, null=True, blank=True, 
                                            help_text="Are you interested in selling your property? (NO/YES)")
    land_or_house = models.CharField(max_length=250, null=True, blank=True, help_text="Is this a Land, or a House?")
    id_number = models.CharField(max_length=250, null=True, blank=True, 
                                 help_text="What is the Id number that is printed on the bottom right corner of your envelope, or letter that we sent you?")
    co_owners = models.CharField(max_length=250, null=True, blank=True,
                                 help_text="Are there any co-owners listed on the deed (spouse,family,business partners)")
    owner = models.CharField(max_length=250, null=True, blank=True,
                             help_text="Are you the owner or Record with the County?")
    good_phone_number = models.CharField(max_length=250, null=True, blank=True, 
                                         help_text="What is a good phone number that we can reach you at if we have any additional questions in the future? ")
    verify_the_information = models.CharField(max_length=250, null=True, blank=True, 
                                              help_text="Let me verify the information that we have:a. Is this address correct?")
    property_to_sell = models.CharField(max_length=250, null=True, blank=True, 
                                        help_text="Is this the property you want to sell (Reference APN)?")
    size_of_the_property = models.CharField(max_length=250, null=True, blank=True, 
                                            help_text="What is the size of the property?")
    hoa_in_this_area = models.CharField(max_length=250, null=True, blank=True,
                                        help_text="Is there an HOA in this area (If so get annual HOA Dues)?")
    own_the_property_free_and_clear = models.CharField(max_length=250, null=True, blank=True, 
                                                       help_text="Do you own the property free and clear?")
    improvements  = models.CharField(max_length=250, null=True, blank=True, 
                                                    help_text="Are there any improvements on the property?")
    electricity = models.CharField(max_length=250, null=True, blank=True, 
                                   help_text="Is there electricity in the property?")
    road_access = models.CharField(max_length=250, null=True, blank=True, 
                                   help_text="Does the property have road access?")
    owned_the_property = models.CharField(max_length=250, null=True, blank=True, 
                                          help_text="How long have you owned the property?")
    pay_cash_and_close = models.CharField(max_length=250, null=True, blank=True, 
                                          help_text="If we can pay cash and close on any date you want, what would be the least that you would take for the property?")
    property_currently_listed = models.CharField(max_length=250, null=True, blank=True, 
                                                 help_text="Is the property currently listed with a Real Estate agent?")
    name_and_phone_number_of_agent = models.CharField(max_length=250, null=True, blank=True, 
                                                      help_text="If yes, Name & Phone Num. of Agent?")
    date_listed = models.DateField(null=True, blank=True, default=datetime.date.today, 
                                   help_text="What was the date you listed it?")
    average_handling_time = models.FloatField(null=True, blank=True, default=0.00)
    additional_comments = models.TextField(null=True, blank=True)
    additional_notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Office Flowers Valley Seller Data"
        verbose_name_plural = "Office Flowers Valley Seller Datas"

    def __str__(self):
        return str(self.customer_care_specialist)

    
class SolidWorkProperties(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    call_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    customer_care_specialist = models.ForeignKey(CustomerCareSpecialist, null=True, blank=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=250, null=True, blank=True, help_text="Name of the Caller.")
    lot_apn_number = models.CharField(max_length=100, null=True, blank=True,
                                      help_text="What is the lot APN number? Where`s the land located?")
    property_owner = models.CharField(max_length=100, null=True, blank=True, 
                                      help_text="Are you the property owner listed on the deed?")
    other_owners = models.CharField(max_length=100, null=True, blank=True, 
                                    help_text="Are there any other owners listed on the deed?")
    phone_number = models.CharField(max_length=100, null=True, blank=True, help_text="What is your Phone number?")
    mailing_address = models.TextField(null=True, blank=True, help_text="What's your Mailing Address?")
    structure = models.CharField(max_length=250, null=True, blank=True, 
                                 help_text="Is there a structure, like perhaps a mobile home or a shed on this property?")
    perc_test = models.CharField(max_length=250, null=True, blank=True, 
                                 help_text="Have you had a perc test done on this lot, and if so, could you send me the documentation to show the perc test results?")
    average_handling_time = models.FloatField(null=True, blank=True, default=0.00)
    additional_notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Solid Work Properties LLC Seller Data"
        verbose_name_plural = "Solid Work Properties LLC Seller Datas"
    
    def __str__(self):
        return str(self.customer_care_specialist)


class NewLeafInvestors(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    call_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    customer_care_specialist = models.ForeignKey(CustomerCareSpecialist, null=True, blank=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=250, null=True, blank=True, help_text="Name of the Caller")
    phone_number = models.CharField(max_length=250, null=True, blank=True, help_text="Phone number of Caller")
    receive_a_letter_or_voicemail = models.CharField(max_length=250, null=True, blank=True, help_text="Did you receive a letter or a voicemail from us?")
    owner_of_record = models.CharField(max_length=250, null=True, blank=True, help_text="Are you the owner of record")
    phone_number_to_reach = models.CharField(max_length=250, null=True, blank=True, 
                                             help_text="What is a good phone number that we can reach you at if we have any additional questions in the future?")
    email_address = models.EmailField(null=True, blank=True, help_text="Do you have an email address that you use frequently?")
    mailing_address = models.CharField(max_length=250, null=True, blank=True, help_text="Ask the Mailing address")
    mailing_address_2 = models.CharField(max_length=250, null=True, blank=True, help_text="Mailing address 2")
    city = models.CharField(max_length=250, null=True, blank=True, help_text="What City?")
    state = models.CharField(max_length=250, null=True, blank=True, help_text="What State?")
    zip_code = models.CharField(max_length=250, null=True, blank=True, help_text="What is the Zip Code")
    apn = models.CharField(max_length=150, null=True, blank=True, help_text="APN (Parcel Number) - referenced on your tax bill. Is there an HOA in this area?")
    own_the_property = models.CharField(max_length=150, null=True, blank=True,
                                        help_text="Do you own the property free and clear? Are there any leins on the property?")
    property_listed = models.CharField(max_length=150, null=True, blank=True, help_text="Is this property listed with a Realtor at this time?")
    state_and_county = models.CharField(max_length=150, null=True, blank=True,
                                        help_text="What State and County is the property in? - Enter their response in the Call Notes")
    average_handling_time = models.FloatField(null=True, blank=True, default=0.00)
    additional_notes = models.TextField(null=True, blank=True)
    opening_spiel = models.TextField(null=True, blank=True)
    closing_spiel = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "New Leaf Investors Seller Data"
        verbose_name_plural = "New Leaf Investors Seller Datas"

    def __str__(self):
        return str(self.customer_care_specialist)


class LibertyLands(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    call_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    customer_care_specialist = models.ForeignKey(CustomerCareSpecialist, null=True, blank=True, on_delete=models.PROTECT)
    contact_information = models.CharField(max_length=250, null=True, blank=True, 
                                           help_text="Have you provided(David Van) with your contact information?(if yes, skip questions below, and takebrief message)")
    reference_number = models.CharField(max_length=150, null=True, blank=True,
                                        help_text="What is the reference  number printed in the upper left corner lower right side of the letter you received")
    name = models.CharField(max_length=250, null=True, blank=True, help_text="What is your(Caller) name?")
    property_owner = models.CharField(max_length=250, null=True, blank=True, help_text="Are you the property owner listed on the deed?")
    other_owners = models.CharField(max_length=250, null=True, blank=True, help_text="Are there any other owners listed on the deed?")
    phone_number = models.CharField(max_length=150, null=True, blank=True, help_text="What is your phone number?")
    email_address = models.EmailField(null=True, blank=True, help_text="What is your email address?")
    offer_amount = models.CharField(max_length=250, null=True, blank=True, help_text="CSR- Is there an offer amount on the letter you received?")
    statisfied_with_the_amount = models.CharField(max_length=250, null=True, blank=True, 
                                                  help_text="Seller:”Yes”. CSR- “ok are you satisfied with the amount offered?")
    methods_listed = models.CharField(max_length=250, null=True, blank=True, 
                                      help_text="Seller: “Yes”CSR- “ok all we need you to do is to sign it and return it to us by any of the methods listed on the letter: email, fax, text or physical mail. The faster you can send it to us, the sooner we can start working on closing for you”.")
    lowest_amount = models.CharField(max_length=250, null=True, blank=True,
                                     help_text="Seller: :”No”. CSR- ”ok, what would be the lowest amount that you can accept if we provide a quick, cash no hassle closing?” ")
    no_offer = models.CharField(max_length=250, null=True, blank=True, help_text="Seller: “no, no offer”")

    class Meta:
        verbose_name = "Liberty Lands Seller Data"
        verbose_name_plural = "Liberty Lands Seller Datas"

    def __str__(self):
        return str(self.customer_care_specialist)


class LynkCapital(models.Model):
    YES_NO_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    WOODED_CLEARED_CHOICES = (
        ('Wooded', 'Wooded'),
        ('Cleared', 'Cleared'),
    )
    MONILE_HOME_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Do not know', 'Do not know'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    call_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    customer_care_specialist = models.ForeignKey(CustomerCareSpecialist, null=True, blank=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=250, null=True, blank=True, help_text="OK great, who am I speaking with please?")
    phone_number = models.CharField(max_length=250, null=True, blank=True,
                                    help_text="What is your number in case we get disconnected?")
    offer_on_property = models.CharField(max_length=250, null=True, blank=True, 
                                         help_text="Are you interested in getting an offer on your property?")
    property_address = models.CharField(max_length=250, null=True, blank=True, help_text="What is the property address")
    city = models.CharField(max_length=250, null=True, blank=True, help_text="What City?")
    state = models.CharField(max_length=250, null=True, blank=True, help_text="What State?")
    zip_code = models.CharField(max_length=250, null=True, blank=True, help_text="What is the Zip Code")
    county = models.CharField(max_length=250, null=True, blank=True, help_text="What county is the property in?")
    letter = models.CharField(max_length=250, null=True, blank=True, help_text="Do you have the letter that we send you handy?")
    apn_number = models.CharField(max_length=250, null=True, blank=True,
                                  help_text="If Yes: OK, there is an APN number on the letter, if I can get that itwould be very helpful.")
    name_on_the_letter = models.CharField(max_length=250, null=True, blank=True,
                                          help_text="If No: Can you tell me what the name on the letter that was sent?")
    water_connections = models.CharField(max_length=10, choices=YES_NO_CHOICES,
                                         null=True, blank=True, help_text="Does the property have Water connections? Y/N")
    electricity = models.CharField(max_length=10, choices=YES_NO_CHOICES, null=True,
                                   blank=True, help_text="Does property have connections for Electricity? Y/N")
    access_to_property = models.CharField(max_length=10, choices=YES_NO_CHOICES, null=True,
                                          blank=True, help_text="Is there a road access to the property? Y/N")
    paved_or_dirt = models.CharField(max_length=10, choices=YES_NO_CHOICES, null=True,
                                     blank=True, help_text="Is there a road access to the property? Y/N")
    structure_on_property = models.CharField(max_length=10, choices=YES_NO_CHOICES, null=True,
                                             blank=True, help_text="Is there a structure on the property? Y/N")
    property_listed_on_realtor = models.CharField(max_length=10, choices=YES_NO_CHOICES, null=True,
                                                  blank=True, help_text="Is the property Listed with a realtor? Y/N")
    property_been_flooded = models.CharField(max_length=10, choices=YES_NO_CHOICES, null=True,
                                             blank=True, help_text="Has the property been Flooded? Y/N")
    property_cleared_or_wooded = models.CharField(max_length=10, choices=WOODED_CLEARED_CHOICES, null=True,
                                                  blank=True, help_text="Is the property Cleared or Wooded?")
    cleared = models.CharField(max_length=10, choices=YES_NO_CHOICES, null=True,
                               blank=True, help_text="If cleared, Does it need to be mowed? Y/N")
    owned_the_property = models.CharField(max_length=250, null=True,
                                          blank=True, help_text="How long have you owned the property for?")
    purchase_acquire_the_property = models.CharField(max_length=250, null=True, blank=True, 
                                                      help_text="How did you purchase/acquire the property?")
    inherited_from = models.CharField(max_length=250, null=True, blank=True,
                                      help_text="If Inherited, from Who (full name)")
    currently_listed = models.CharField(max_length=10, choices=YES_NO_CHOICES, null=True, blank=True,
                                        help_text="Are you the person that is currently listed on the deed as the owner on the county records? Y/N")
    if_not_then_who = models.CharField(max_length=250, null=True, blank=True, help_text="If not, then who?")
    hoa = models.CharField(max_length=10, choices=YES_NO_CHOICES, null=True, blank=True,
                           help_text="Are there HOA fees? Y/N")
    property_taxes = models.CharField(max_length=10, choices=YES_NO_CHOICES, null=True, blank=True,
                                      help_text="Are the property taxes current? Y/N")
    if_not_current = models.CharField(max_length=250, null=True, blank=True, help_text="if not current, how much behind?")
    liens = models.CharField(max_length=10, choices=YES_NO_CHOICES, null=True, blank=True,
                             help_text="Do you know if there is any liens including city or state liens against the property? Y/N")
    mobile_homes_allowed = models.CharField(max_length=10, choices=MONILE_HOME_CHOICES, null=True, blank=True,
                                            help_text="Are Mobile Homes Allowed? Y/N or Do not know")
    original_plans = models.CharField(max_length=250, null=True, blank=True, help_text="What were your original plans with the property?")
    interested_in_selling = models.CharField(max_length=250, null=True, blank=True, help_text="Why are you interested in selling now?")
    asking_price = models.CharField(max_length=10, choices=YES_NO_CHOICES, null=True, blank=True,
                                    help_text="Do you have an asking price for the property? Y/N")
    if_yes_how_much = models.CharField(max_length=150, null=True, blank=True, help_text="if yes, how much?")
    best_day_time_to_call = models.CharField(max_length=150, null=True, blank=True, 
                                             help_text="What is the best days and time to call you back to discuss our offer")
    best_number_to_call = models.CharField(max_length=150, null=True, blank=True,
                                           help_text="What is the best number to call you back?")
    average_handling_time = models.FloatField(null=True, blank=True, default=0.00)
    additional_notes = models.TextField(null=True, blank=True)
    opening_spiel = models.TextField(null=True, blank=True)
    received_a_letter_spiel = models.TextField(null=True, blank=True)
    before_spiel = models.TextField(null=True, blank=True)
    handover_spiel = models.TextField(null=True, blank=True)
    closing_spiel = models.TextField(null=True, blank=True)
    faq = models.TextField(null=True, blank=True, verbose_name="FAQ")

    class Meta:
        verbose_name = "Lynk Capital Seller Data"
        verbose_name_plural = "Lynk Capital Seller Datas"

    def __str__(self):
        return str(self.customer_care_specialist)


class DreamCloudBuyLand(models.Model):
    YES_NO_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    call_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    customer_care_specialist = models.ForeignKey(CustomerCareSpecialist, null=True, blank=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=150, null=True, blank=True, help_text="May I have your name please?")
    phone_number = models.CharField(max_length=150, null=True, blank=True,
                                    help_text="Thank you. May I have your phone number in case we get disconnected?")
    interested_in_selling = models.CharField(max_length=10, choices=YES_NO_CHOICES, null=True, blank=True,
                                             help_text="Ok great! Thank you for responding to our letter. Are you interested in selling your property? (YES/NO)")
    number_at_the_bottom_right = models.CharField(max_length=150, null=True, blank=True,
                                                  help_text="What is the number at the bottom right hand corner of your letter?")
    best_address = models.CharField(max_length=150, null=True, blank=True,
                                    help_text="Did we mail our letter to the best address for you? (If yes, do not collect address)*If not, what address should we use?")
    owner_of_record = models.CharField(max_length=150, null=True, blank=True,
                                       help_text="Are you the owner of record? ")
    additional_owners = models.CharField(max_length=150, null=True, blank=True,
                                         help_text="Are there any additional owners?")
    own_the_property_free_and_clear = models.CharField(max_length=150, null=True, blank=True,
                                                       help_text="Do you own the property free and clear?")
    other_information = models.TextField(null=True, blank=True,
                                         help_text="Is there any other information you'd like to share about the property before we send you our offer? (note comments) ")
    additional_comments = models.TextField(null=True, blank=True)
    average_handling_time = models.FloatField(null=True, blank=True, default=0.00)
    additional_notes_from_csr = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Dream Cloud Buy Land Seller Data"
        verbose_name_plural = "Dream Cloud Buy Land Seller Datas"

    def __str__(self):
        return str(self.customer_care_specialist)


class LandQuestPro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    call_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    customer_care_specialist = models.ForeignKey(CustomerCareSpecialist, null=True, blank=True, on_delete=models.PROTECT)
    caller_name = models.CharField(max_length=150, null=True, blank=True, help_text="Caller's Name")
    phone_number = models.CharField(max_length=150, null=True, blank=True, help_text="Caller's Phone number")
    other_owners = models.CharField(max_length=150, null=True, blank=True,
                                    help_text="Are there any other owners listed on the title for the property?")
    reference_number = models.CharField(max_length=150, null=True, blank=True,
                                        help_text="Can you please tell me the reference number on the offer letter you received in the mail? You will find it on the upper left area of the page.")
    prefer_to_contact = models.CharField(max_length=150, null=True, blank=True,
                                         help_text="Do you prefer for us to contact you via phone call,texting or email? If email could you please provide me that information?")
    other_details = models.CharField(max_length=150, null=True, blank=True,
                                     help_text="Are there any other details about your parcel that you feel would be helpful for us to know before we start doing our homework?")
    other_properties = models.CharField(max_length=150, null=True, blank=True,
                                        help_text="Do you have any other properties that you are looking to sell? If so, can you email or text me the County, State, APN for each?” (They may also submit the property at www.landquestpro.com)")
    last_questions = models.CharField(max_length=150, null=True, blank=True,
                                      help_text="Do you have any last questions that you would like me to forward before I let you go?")
    average_handling_time = models.FloatField(null=True, blank=True, default=0.00)
    additional_notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Land Quest Pro Seller Data"
        verbose_name_plural = "Land Quest Pro Seller Datas"

    def __str__(self):
        return str(self.customer_care_specialist)


class LandRapid(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    call_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    customer_care_specialist = models.ForeignKey(CustomerCareSpecialist, null=True, blank=True, on_delete=models.PROTECT)
    caller_name = models.CharField(max_length=150, null=True, blank=True, help_text="Caller's Name")
    phone_number = models.CharField(max_length=150, null=True, blank=True, help_text="Caller's Phone number")
    email_address = models.EmailField(null=True, blank=True)
    offer_price_listed = models.CharField(max_length=150, null=True, blank=True, 
                                          help_text="Do you accept the offer price listed on the letter?")
    owner_name = models.CharField(max_length=150, null=True, blank=True,
                                  help_text="Owner(s) Name (as on deed)")
    relationship = models.CharField(max_length=150, null=True, blank=True,
                                    help_text="Relationship (to contact)")
    other_co_owners = models.CharField(max_length=150, null=True, blank=True,
                                       help_text="Are there any other co-owners listed on the deed (spouse, family, business partner)?")
    signers = models.CharField(max_length=150, null=True, blank=True,
                               help_text="Are the Signers (Sellers) available to sign at one time?")
    how_did_you_aquire_the_property = models.CharField(max_length=150, null=True, blank=True,
                                           help_text="How did you acquire this property (purchased, inherited, divorce settlement, other)?")
    when_did_you_aquire_the_property = models.CharField(max_length=150, null=True, blank=True,
                                                        help_text="When did you acquire this property?")
    title_issues = models.CharField(max_length=150, null=True, blank=True, help_text="Any Title Issues?")
    back_taxes_on_the_property = models.CharField(max_length=150, null=True, blank=True, 
                                                  help_text="Are there any back-taxes on the property?")
    selling_the_property = models.CharField(max_length=150, null=True, blank=True,
                                            help_text="Why are you selling this property?")
    state_property_located = models.CharField(max_length=150, null=True, blank=True,
                                              help_text="What State is the Property Located In?")
    county_property_located = models.CharField(max_length=150, null=True, blank=True,
                                               help_text="What County is the Property Located In?")
    city_property_located = models.CharField(max_length=150, null=True, blank=True,
                                             help_text="What City is the Property Located In?")
    address_or_parcel_id = models.CharField(max_length=150, null=True, blank=True,
                                            help_text="What is the Property’s Address or Parcel ID (it should be in the letter i sent them)?")
    size_and_dimensions = models.CharField(max_length=150, null=True, blank=True,
                                           help_text="What is the size and dimensions of this parcel of land (in acres)?")
    road_access = models.CharField(max_length=150, null=True, blank=True,
                                   help_text="Is there road access to this property (dirt or paved)?")
    utilities = models.CharField(max_length=150, null=True, blank=True,
                                 help_text="What utilities are available to this property (water, well, sewer, septic, electricity, natural gas)?")
    other_improvements = models.CharField(max_length=150, null=True, blank=True,
                                          help_text="Are there any other improvements on this property (fence, slab, shed, other)?")
    any_structures = models.CharField(max_length=150, null=True, blank=True,
                                      help_text="Are there any structures on the Property")
    mortgages_or_liens = models.CharField(max_length=150, null=True, blank=True,
                                          help_text="Do you know of any mortgages or liens on this property (if so, what will it take to pay them off)?")
    hoa = models.CharField(max_length=150, null=True, blank=True,
                           help_text="Is this property part of an HOA (Home Owners’ Association)? If so, what are the annual fees? Are there any specific property restrictions?")
    current_zoning = models.CharField(max_length=150, null=True, blank=True,
                                      help_text="What is the current zoning on this property (i.e. – what can it be used for)?")
    currently_listed = models.CharField(max_length=150, null=True, blank=True,
                                        help_text="Is this property currently listed with a Realtor (and if so, can I get their contact information)?")
    about_the_property = models.CharField(max_length=150, null=True, blank=True,
                                          help_text="Is there anything we should know about the property? (I’m looking for good or bad things about the area).")
    own_any_other_properties = models.CharField(max_length=150, null=True, blank=True, 
                                                help_text="Do you own any other properties that you’d like to sell?")
    should_note = models.CharField(max_length=150, null=True, blank=True,
                                   help_text="Is there anything else I should note or any other comments?")
    average_handling_time = models.FloatField(null=True, blank=True, default=0.00)
    additional_notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Land Rapid Seller Data"
        verbose_name_plural = "Land Rapid Seller Datas"

    def __str__(self):
        return str(self.customer_care_specialist)


class Alevi(models.Model):
    UTILITIES_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('In Area', 'In Area'),
        ('Not Sure', 'Not Sure')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    call_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    customer_care_specialist = models.ForeignKey(CustomerCareSpecialist, null=True, blank=True, on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=150, null=True, blank=True, help_text="Phone number of the Caller")
    reference_number = models.CharField(max_length=150, null=True, blank=True,
                                        help_text="Can you provide us with the reference number from the letter? (APN) ")
    owner_of_record = models.CharField(max_length=150, null=True, blank=True,
                                       help_text="You are the owner of record with the county, that information we had was correct? (either write yes if they are or any other owner information they provide – no need to ask follow up questions)")
    interested_in_selling = models.CharField(max_length=150, null=True, blank=True,
                                             help_text="And you are interested in selling it? (write down comments what they say)")
    several_properties = models.CharField(max_length=150, null=True, blank=True,
                                          help_text="Do you own one or several properties (if several please write down the info they provide like address and county).")
    size = models.CharField(max_length=150, null=True, blank=True,
                            help_text="What size is the property – is it a building lot or an acerage?")
    road_access = models.CharField(max_length=150, null=True, blank=True,
                                   help_text="Does it have road access and if so is it paved or unpaved?")
    utilities = models.CharField(max_length=15, choices=UTILITIES_CHOICES, null=True, blank=True,
                                 help_text="Are there utilities at the property?")
    improvements = models.CharField(max_length=150, null=True, blank=True,
                                    help_text="Are there any improvements to the property? (just write down any comments they make)")
    owned_the_property = models.CharField(max_length=150, null=True, blank=True,
                                          help_text="How long have you owned the property?")
    back_taxes = models.CharField(max_length=150, null=True, blank=True,
                                  help_text="How long have you owned the property?")
    owners_association = models.CharField(max_length=150, null=True, blank=True,
                                          help_text="Is the property part of a home owners association? (if yes, please ask for the name of the home owners association and annual fees)")
    listed_with_real_estate_agent = models.CharField(max_length=150, null=True, blank=True,
                                                     help_text="Is the property currently listed with a Real Estate Agent? (if yes, please ask for how much it is listed for and for how long)?")
    last_question = models.CharField(max_length=150, null=True, blank=True,
                                     help_text="(word for word – last question): So at this point – what are you trying to do – are you trying to get rid of it or do you have a number in mind what you wanted to get for the property? (write down their comments and ideally an expected number) ")
    average_handling_time = models.FloatField(null=True, blank=True, default=0.00)
    additional_notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Alevi Seller Data"
        verbose_name_plural = "Alevi Seller Datas"

    def __str__(self):
        return str(self.customer_care_specialist)


class AffordaleLandInvestment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    call_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    customer_care_specialist = models.ForeignKey(CustomerCareSpecialist, null=True, blank=True, on_delete=models.PROTECT)
    contact_information = models.CharField(max_length=150, null=True, blank=True, 
                                           help_text="Have you provided the office of Adam Harrison with your contact information? (if yes, skip questions below, and take a brief message)")
    name = models.CharField(max_length=150, null=True, blank=True, help_text="What is your name?")
    state_county = models.CharField(max_length=150, null=True, blank=True, 
                                    help_text="What state and county is your property located in?")
    parcel_number = models.CharField(max_length=150, null=True, blank=True,
                                     help_text="Do you know what the parcel number of the property is, it is located on the second page of the letter if you got a letter")
    property_owner = models.CharField(max_length=150, null=True, blank=True,
                                      help_text="Are you the property owner listed on the deed?")
    other_owners = models.CharField(max_length=150, null=True, blank=True,
                                    help_text="Are there any other owners listed on the deed?(If others on the deed, ask the following question)")
    sell_the_property = models.CharField(max_length=150, null=True, blank=True,
                                         help_text="Have you and the others on the deed all decided to sell the property?")
    phone_number = models.CharField(max_length=150, null=True, blank=True,
                                    help_text="What is your phone number?")
    email_address = models.EmailField(null=True, blank=True, help_text="What is your email address?")
    listed_in_letter_or_postcard = models.CharField(max_length=150, null=True, blank=True,
                                                    help_text="Do you want to sell at the price listed on the letter or the postcard you received? ( If they say no to this question ask them the following:) ")
    for_your_property = models.CharField(max_length=150, null=True, blank=True,
                                         help_text="If we were to pay all cash and close within the next 10 days, what is the least you would accept for your property?")
    average_handling_time = models.FloatField(null=True, blank=True, default=0.00)
    additional_notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Affordable Land Investment Seller Data"
        verbose_name_plural = "Affordable Land Investment Seller Datas"

    def __str__(self):
        return str(self.customer_care_specialist)


class LGPropertyVentures(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    call_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    customer_care_specialist = models.ForeignKey(CustomerCareSpecialist, null=True, blank=True, on_delete=models.PROTECT)
    reference_number = models.CharField(max_length=250, null=True, blank=True,
                                        help_text="WHAT IS THE REFERENCE NUMBER ON THE TOP OF YOUR LETTER PLEASE? THIS WILL ASSIST US IN GETTING TO THE OFFER OUT TO YOU? ")
    property_owner = models.CharField(max_length=250, null=True, blank=True,
                                      help_text="ARE YOU THE PROPERTY OWNER OR I NEED EVERYONES NMAE THATS ON THE DEED?")
    access = models.CharField(max_length=150, null=True, blank=True,
                              help_text="DOES THE PROPERTY HAVE ACCESS TO POWER, WATER OR SEWER? ")
    selling_your_property = models.CharField(max_length=150, null=True, blank=True,
                                             help_text="SIR/MAME AND WHY ARE YOU SELLING YOUR PROPERTY?")
    average_handling_time = models.FloatField(null=True, blank=True, default=0.00)
    additional_notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "LG Property Ventures Seller Data"
        verbose_name_plural = "LG Property Ventures Seller Datas"

    def __str__(self):
        return str(self.customer_care_specialist)


class FranklinManagement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    call_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    customer_care_specialist = models.ForeignKey(CustomerCareSpecialist, null=True, blank=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=150, null=True, blank=True, help_text="What is your name?")
    property_owner = models.CharField(max_length=150, null=True, blank=True, 
                                      help_text="Are you the property owner listed on the deed?")
    other_owner = models.CharField(max_length=150, null=True, blank=True,
                                   help_text="Are there any other owners listed on the deed?")
    phone_number = models.CharField(max_length=150, null=True, blank=True,
                                    help_text="What is your phone number? ")
    email_address = models.EmailField(null=True, blank=True, help_text="What is your email?")
    road_access = models.CharField(max_length=150, null=True, blank=True,
                                   help_text="Does the property have road access?")
    property_currently_listed = models.CharField(max_length=150, null=True, blank=True,
                                                 help_text="Is the property currently listed with a real estate agent?")
    utilities = models.CharField(max_length=150, null=True, blank=True,
                                 help_text="Are there utilities available at the property?")
    consider_selling_it = models.CharField(max_length=150, null=True, blank=True,
                                           help_text="This is a nice property, why would you ever consider selling it? ")
    improvements = models.CharField(max_length=150, null=True, blank=True,
                                    help_text="Does the property have any improvements?")
    hoa_poa = models.CharField(max_length=150, null=True, blank=True,
                               help_text="Is there a HOA/POA?")
    back_taxes = models.CharField(max_length=150, null=True, blank=True,
                                  help_text="Are there any back taxes on the property?")
    liens_in_property = models.CharField(max_length=150, null=True, blank=True,
                                         help_text="Any other liens on the property?")
    lowest_number = models.CharField(max_length=150, null=True, blank=True,
                                     help_text="what is the lowest number you are willing to take?")
    closing_date = models.DateField(null=True, blank=True, help_text="Are you okay with up to a 6 month closing date?")
    other_properties = models.CharField(max_length=150, null=True, blank=True,
                                        help_text="Do you have other properties that you would consider selling?")
    know_about_the_property = models.CharField(max_length=150, null=True, blank=True,
                                               help_text="Anything else we should know about the property?")
    average_handling_time = models.FloatField(null=True, blank=True, default=0.00)
    additional_notes = models.TextField(null=True, blank=True)
    opening_spiel = models.TextField(null=True, blank=True)
    closing_spiel = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Franklin Management Seller Data"
        verbose_name_plural = "Franklin Management Seller Datas"

    def __str__(self):
        return str(self.customer_care_specialist)
