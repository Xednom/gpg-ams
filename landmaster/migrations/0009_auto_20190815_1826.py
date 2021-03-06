# Generated by Django 2.1.2 on 2019-08-15 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landmaster', '0008_changed_urlfield_to_charfield_for_urlfields'),
    ]

    operations = [
        migrations.AddField(
            model_name='duediligence',
            name='city_or_mud_district',
            field=models.TextField(blank=True, help_text='Is the property in the city or MUD district? Is there water to the property. If no, do we have to dig a well or there are city water?', null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='electricity_connected',
            field=models.TextField(blank=True, help_text='Does property Currently Have Electricty connected', null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='hoa',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='land_cleared',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='liens_on_property',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='no_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='no_power',
            field=models.TextField(blank=True, help_text='If No Power (electricity)? Is there power to the lot? If no, how far away is the nearest power line? If they know, how much it cost to connect to the power line?', null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='parcel_dimensions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='property_buildable',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='structure',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='subdivision',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='tax_amount',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='water_connected',
            field=models.TextField(blank=True, help_text='Does the property have water connected? If Yes: City Water, Well', null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='water_to_property',
            field=models.TextField(blank=True, help_text='If No: Water?Is there water to the property. If no, do we have to dig a well or there are city water?', null=True),
        ),
        migrations.AlterField(
            model_name='duediligence',
            name='assessors_office_contact',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='duediligence',
            name='tax_office_contact',
            field=models.TextField(blank=True, null=True),
        ),
    ]
