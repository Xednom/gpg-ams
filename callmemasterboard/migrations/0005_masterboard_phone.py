# Generated by Django 2.1.2 on 2019-06-30 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callmemasterboard', '0004_auto_20190630_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterboard',
            name='phone',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
