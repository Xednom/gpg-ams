# Generated by Django 2.1.2 on 2019-05-21 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landmaster', '0008_auto_20190521_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duediligence',
            name='initial_due_diligence_completion',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Completion – Initial Data'),
        ),
    ]