# Generated by Django 2.1.2 on 2019-04-16 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190409_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffs',
            name='position',
            field=models.CharField(blank=True, choices=[('Senior Operations Managers', 'Senior Operations Managers'), ('Project Managers', 'Project Managers'), ('Team Leads', 'Team Leads'), ('General Administrative Support', 'General Administrative Support')], max_length=150, null=True),
        ),
    ]