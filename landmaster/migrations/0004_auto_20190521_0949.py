# Generated by Django 2.1.2 on 2019-05-21 01:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('landmaster', '0003_auto_20190520_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='duediligence',
            name='date_of_completion',
            field=models.DateField(blank=True, help_text='Date of Completion Submitted to the Client- Overall Due Diligence', null=True),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='operator_details_other_requests',
            field=models.TextField(blank=True, null=True, verbose_name='County Operator Details - Other Requests'),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='operator_details_tax_data',
            field=models.TextField(blank=True, null=True, verbose_name='County Operator Details - Tax Data'),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='operator_details_utilities_data',
            field=models.TextField(blank=True, null=True, verbose_name='County Operator Details - Utilities Data'),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='operator_details_zoning_data',
            field=models.TextField(blank=True, null=True, verbose_name='County Operator Details - Zoning Data'),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='other_requests_completion',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date of Completion – Other Requests'),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='status_initial_data',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Due Diligence Status for Initial Data'),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='status_other_requests',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Due Diligence Status for Other Requests'),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='status_tax_data',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Due Diligence Status for Tax Data'),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='status_utilities_data',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Due Diligence Status for Utilities Data'),
        ),
        migrations.AddField(
            model_name='duediligence',
            name='status_zoning_data',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Due Diligence Status for Zoning Data'),
        ),
        migrations.AlterField(
            model_name='duediligence',
            name='initial_due_diligence_completion',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date of Completion – Initial Data'),
        ),
        migrations.AlterField(
            model_name='duediligence',
            name='tax_data_completion',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date of Completion – Tax Data'),
        ),
        migrations.AlterField(
            model_name='duediligence',
            name='utilities_data_completion',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date of Completion – Utilities Data'),
        ),
        migrations.AlterField(
            model_name='duediligence',
            name='zoning_data_completion',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date of Completion – Zoning Data'),
        ),
    ]