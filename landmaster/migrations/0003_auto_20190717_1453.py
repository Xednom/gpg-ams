# Generated by Django 2.1.2 on 2019-07-17 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landmaster', '0002_auto_20190611_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duediligence',
            name='project_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.Staffs'),
        ),
    ]
