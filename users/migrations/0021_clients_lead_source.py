# Generated by Django 2.1.2 on 2019-06-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20190604_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='lead_source',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
