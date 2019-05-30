# Generated by Django 2.1.2 on 2019-05-30 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_auto_20190430_2008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lynkcapital',
            options={'verbose_name': 'Lynk Capital Seller Data', 'verbose_name_plural': 'Lnyk Capital Seller Datas'},
        ),
        migrations.AddField(
            model_name='lynkcapital',
            name='before_spiel',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lynkcapital',
            name='closing_spiel',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lynkcapital',
            name='opening_spiel',
            field=models.TextField(blank=True, null=True),
        ),
    ]
