# Generated by Django 2.1.2 on 2019-03-08 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['-date_sign_up'], 'verbose_name': 'List of Client Job', 'verbose_name_plural': 'List of Client Jobs'},
        ),
    ]
