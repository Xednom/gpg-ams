# Generated by Django 2.1.2 on 2019-03-22 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeBuyAcreageLlc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_date', models.DateField(blank=True, null=True)),
                ('contact_information', models.CharField(blank=True, help_text='Have you provided (Jeff) with your contact information? (if yes, skip questions below, and take a brief message)', max_length=250, null=True)),
                ('address_or_apn', models.TextField(blank=True, help_text='What is the address of the property you are interested in?(If the caller does NOT have the property address, ask them...)What is the APN number?', null=True)),
                ('name_of_the_caller', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_number_of_caller', models.CharField(blank=True, max_length=250, null=True)),
                ('are_you_an_agent', models.CharField(blank=True, max_length=250, null=True)),
                ('listing', models.CharField(blank=True, help_text='Where did you see the listing?', max_length=250, null=True)),
                ('your_phone_number', models.CharField(blank=True, help_text='What is your Phone number?', max_length=250, null=True)),
                ('email_address', models.EmailField(blank=True, help_text='What is your email address', max_length=250, null=True)),
                ('average_handling_time', models.CharField(blank=True, help_text='Average Handling Time', max_length=250, null=True)),
                ('additional_notes', models.TextField(blank=True, null=True)),
                ('customer_care_specialist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='buyer.CustomerCareSpecialist')),
            ],
            options={
                'verbose_name': 'We Buy Acreage LLC',
            },
        ),
    ]