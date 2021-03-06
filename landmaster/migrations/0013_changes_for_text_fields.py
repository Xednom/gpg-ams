# Generated by Django 2.1.2 on 2019-09-17 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landmaster', '0012_auto_20190816_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duediligence',
            name='assessor_website',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='duediligence',
            name='cad_website',
            field=models.TextField(blank=True, null=True, verbose_name='CAD Website'),
        ),
        migrations.AlterField(
            model_name='duediligence',
            name='gis_website',
            field=models.TextField(blank=True, null=True, verbose_name='GIS Website'),
        ),
        migrations.AlterField(
            model_name='duediligence',
            name='google_map_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='duediligence',
            name='gps_coordinates',
            field=models.TextField(blank=True, null=True, verbose_name='GPS Coordinates'),
        ),
        migrations.AlterField(
            model_name='duediligence',
            name='gps_coordinates_4_corners',
            field=models.TextField(blank=True, null=True, verbose_name='GPS Coordinates 4 Corners'),
        ),
        migrations.AlterField(
            model_name='duediligence',
            name='recorder_clerk_website',
            field=models.TextField(blank=True, null=True, verbose_name='Recorder/Clerk Website'),
        ),
        migrations.AlterField(
            model_name='duediligence',
            name='time_limit_to_build',
            field=models.TextField(blank=True, help_text='Is there any time limit to build?', null=True),
        ),
        migrations.AlterField(
            model_name='duediligence',
            name='treasurer_website',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='duediligence',
            name='zoning_department_website',
            field=models.TextField(blank=True, null=True),
        ),
    ]
