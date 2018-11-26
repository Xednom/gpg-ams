# Generated by Django 2.1.2 on 2018-11-25 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reporting', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0002_auto_20181125_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='assigned_job_request_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='report',
            name='clients_full_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.ClientName'),
        ),
        migrations.AddField(
            model_name='report',
            name='job_requested_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reporting.Job'),
        ),
        migrations.AddField(
            model_name='report',
            name='project_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='client.ProjectManager'),
        ),
        migrations.AddField(
            model_name='report',
            name='week_to_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reporting.WeekToDate'),
        ),
    ]