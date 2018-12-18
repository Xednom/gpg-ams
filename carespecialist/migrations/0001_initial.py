# Generated by Django 2.1.2 on 2018-12-16 14:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='care_specialist_report',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name_appeared_from_letter', models.CharField(max_length=250, verbose_name='Company name or Name appread from Letter received')),
                ('care_specialist', models.CharField(blank=True, max_length=250, null=True)),
                ('date_of_the_lead_called', models.DateField(blank=True, null=True)),
                ('full_name_of_the_caller', models.CharField(blank=True, max_length=250, null=True)),
                ('caller_id', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=250, null=True)),
                ('receive_letter', models.CharField(blank=True, max_length=100, null=True, verbose_name='Did you receive a letter from us?(IF YES, PROCEED TO THE NEXT QUESTION)')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='IF NO, DO NOT PROCEED AND JUST ASK THE CONCERN OF THE CALLER')),
                ('property_located', models.CharField(blank=True, max_length=250, null=True, verbose_name='Where is the property located? Please specify the county & state?')),
                ('apn_property_id', models.CharField(blank=True, max_length=250, null=True, verbose_name='What is the property APN/property ID, including the dashes?')),
                ('selling_property', models.CharField(blank=True, max_length=250, null=True, verbose_name='Are you interested in selling this property? (If yes, continue with script. If NO ask the question below)')),
                ('price_looking_to_get_property', models.CharField(blank=True, max_length=250, null=True, verbose_name=' What price are you looking to get for the property?')),
                ('owner_of_the_property', models.CharField(blank=True, max_length=250, null=True, verbose_name="Are you the owner of the property as per county's record? If No: Ask the question below.")),
                ('name_on_the_record', models.TextField(blank=True, null=True, verbose_name='May I ask whose name is on reord with the county?')),
                ('mailed_from', models.CharField(blank=True, max_length=100, null=True, verbose_name='Is the address we mailed from letter we sent is correct? If no: please ask the question below.')),
                ('mailing_address', models.TextField(blank=True, null=True, verbose_name='What is your mailing address?')),
                ('contact_number', models.TextField(blank=True, null=True, verbose_name='Is this the best ccontact number that we can reach you? (Please verify phone number with the caller - read back to them)')),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True, verbose_name='May I have your emaill address?')),
                ('properties', models.CharField(blank=True, max_length=250, null=True, verbose_name='Do you own one or several properties you would like to sell? If several: please ask the question below.')),
                ('apn_counties', models.TextField(blank=True, null=True, verbose_name="Please gather all the APN's and counties of the properties they would like to sell.")),
                ('taxes', models.CharField(blank=True, max_length=250, null=True, verbose_name='Are the  taxes up to date or paid?If not up to date please ask for the current total amount due')),
                ('total_current_amount_due', models.TextField(blank=True, null=True, verbose_name='Total Current Amount Due?')),
                ('special_attribute', models.TextField(blank=True, null=True, verbose_name='Any special attibutes of the property? Water well, near power pole or treed, easy road access, etc)')),
                ('info_on_the_property', models.TextField(blank=True, null=True, verbose_name='Is there anything else you would like to tell us about this property?')),
                ('extra_comments', models.TextField(blank=True, null=True, verbose_name='Notes if caller says extra comments:')),
                ('email_sent_to_the_owner', models.CharField(blank=True, max_length=250, null=True, verbose_name='Eamil sent to the Owner?')),
                ('calendar_invite', models.CharField(blank=True, max_length=250, null=True, verbose_name='Calendar Invite Sent to the Owner? ( In case of Hot Leads)')),
                ('total_minutes_answered', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Total Minutes Answered')),
            ],
            options={
                'ordering': ['-name_appeared_from_letter'],
            },
        ),
    ]
