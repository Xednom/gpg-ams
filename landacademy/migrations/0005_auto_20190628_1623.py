# Generated by Django 2.1.2 on 2019-06-28 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('landacademy', '0004_auto_20190628_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='landacademyinventory',
            old_name='date_paid',
            new_name='date_payment_made',
        ),
        migrations.RemoveField(
            model_name='landacademyinventory',
            name='pivot_table',
        ),
        migrations.RemoveField(
            model_name='landacademyinventory',
            name='project_status',
        ),
        migrations.AddField(
            model_name='landacademyinventory',
            name='client_la_requestor',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Client LA Requestor'),
        ),
        migrations.AddField(
            model_name='landacademyinventory',
            name='complete_order',
            field=models.URLField(blank=True, null=True, verbose_name='Complete Order - URL Link'),
        ),
        migrations.AddField(
            model_name='landacademyinventory',
            name='date_requested',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='landacademyinventory',
            name='order_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Order Name/Number'),
        ),
        migrations.AddField(
            model_name='landacademyinventory',
            name='status_of_order',
            field=models.CharField(blank=True, choices=[('Completed', 'Completed'), ('In Progress', 'In Progress')], max_length=150, null=True, verbose_name='Status of the Order'),
        ),
        migrations.AddField(
            model_name='landacademyinventory',
            name='total_charge',
            field=models.DecimalField(decimal_places=2, default=1, help_text='Total Charge + Total PP Fee', max_digits=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landacademyinventory',
            name='total_items_charge',
            field=models.DecimalField(decimal_places=2, default=3, help_text='Total Items Requested x $.10', max_digits=7, verbose_name='Total Charge'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landacademyinventory',
            name='total_items_requested',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='landacademyinventory',
            name='total_pp_fee',
            field=models.DecimalField(decimal_places=2, default=56, help_text='Total Charge *.05', max_digits=7, verbose_name='Total PP Fee'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='landacademyinventory',
            name='invoice',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Invoice # Towards LA'),
        ),
    ]