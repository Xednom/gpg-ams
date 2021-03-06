# Generated by Django 2.1.2 on 2019-08-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobrequest', '0002_auto_20190816_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobrequest',
            name='additional_mem0',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobrequest',
            name='project_status',
            field=models.CharField(blank=True, choices=[('Sent to Project Manager', 'Sent to Project Manager'), ('Sent to Virtual Assistant', 'Sent to Virtual Assistant'), ('VA Processing', 'VA Processing'), ('VA Completed Job Request', 'VA Completed Job Request'), ('Submit to Project Manager for Quality Purposes', 'Submit to Project Manager for Quality Purposes'), ('Job Request submitted to Client', 'Job Request submitted to Client'), ('Job Request Closed', 'Job Request Closed')], max_length=150, null=True),
        ),
    ]
