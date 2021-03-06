# Generated by Django 2.1.2 on 2019-06-30 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callmemasterboard', '0003_masterboard_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterboard',
            name='client_folder',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name="Clients's Folder"),
        ),
        migrations.AddField(
            model_name='masterboard',
            name='email',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='masterboard',
            name='gs_integration',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='GS Integration'),
        ),
        migrations.AlterField(
            model_name='masterboard',
            name='url_buyer',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='masterboard',
            name='url_property_management',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='masterboard',
            name='url_seller',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
