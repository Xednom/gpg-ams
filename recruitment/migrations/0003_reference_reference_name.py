# Generated by Django 2.1.2 on 2019-05-29 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0002_auto_20190529_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='reference_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]