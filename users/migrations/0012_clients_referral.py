# Generated by Django 2.1.2 on 2019-04-20 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190420_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='referral',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]