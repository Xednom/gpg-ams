# Generated by Django 2.1.2 on 2019-03-29 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fillables', '0002_added_va'),
        ('jobrequest', '0003_revised_job_request_app'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobrequest',
            name='company_assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fillables.InternalCompanyName'),
        ),
        migrations.AddField(
            model_name='jobrequest',
            name='company_billable_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fillables.CompanyName'),
        ),
    ]