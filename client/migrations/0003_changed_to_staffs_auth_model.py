# Generated by Django 2.1.2 on 2019-06-10 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20190309_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='VA_assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.Staffs'),
        ),
    ]
