# Generated by Django 2.1.2 on 2019-08-03 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callmemasterboard', '0010_added_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterboard',
            name='client_folder',
            field=models.TextField(blank=True, null=True, verbose_name="Clients's Folder"),
        ),
        migrations.AlterField(
            model_name='masterboard',
            name='gs_integration',
            field=models.TextField(blank=True, null=True, verbose_name='GS Integration'),
        ),
    ]
