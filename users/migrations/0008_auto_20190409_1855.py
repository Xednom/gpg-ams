# Generated by Django 2.1.2 on 2019-04-09 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190409_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_client',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
