# Generated by Django 2.1.2 on 2019-07-24 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landmaster', '0006_added_client_request_text_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='duediligence',
            name='total_hrs_for_initial_dd',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='total_hrs_overall_dd_callouts',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='total_time_allocation',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7, null=True),
        ),
    ]
