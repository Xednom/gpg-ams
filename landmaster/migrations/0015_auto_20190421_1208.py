# Generated by Django 2.1.2 on 2019-04-21 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landmaster', '0014_auto_20190420_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duediligence',
            name='status_of_dd',
            field=models.CharField(blank=True, choices=[('Project Managers Review', 'Project Managers Review'), ('Submitted to the Client', 'Submitted to the Client'), ('Approved by the Client', 'Approved by the Client'), ('Sent to Project Manager', 'Sent to Project Manager'), ('Project Managers Review', 'Project Managers Review'), ('Sent to VA', 'Sent to VA'), ('VA Processing', 'VA Processing'), ('Sent to Quality Specialist', 'Sent to Quality Specialist'), ('Quality Specialist Checking', 'Quality Specialist Checking'), ('Submitted to the Client', 'Submitted to the Client'), ('Approved by the Client', 'Approved by the Client')], max_length=150, null=True),
        ),
    ]
