# Generated by Django 2.1.2 on 2019-08-12 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190803_1716'),
        ('craigslist', '0003_auto_20190711_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='craiglistinventory',
            name='client_company_name',
        ),
        migrations.AddField(
            model_name='craiglistinventory',
            name='client_name_company_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.Clients'),
        ),
        migrations.AlterField(
            model_name='craiglistinventory',
            name='cl_admin_support',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.Staffs'),
        ),
    ]