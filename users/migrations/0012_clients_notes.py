# Generated by Django 2.1.2 on 2019-09-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190803_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]