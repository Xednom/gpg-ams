# Generated by Django 2.1.2 on 2019-06-30 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callmeinventory', '0008_auto_20190625_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='crm_login',
            field=models.TextField(blank=True, null=True, verbose_name='CRM System - Log In Information'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='phone_login',
            field=models.TextField(blank=True, null=True, verbose_name='Phone System - Log In Information'),
        ),
    ]