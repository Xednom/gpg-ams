# Generated by Django 2.1.2 on 2019-07-19 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190719_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffs',
            name='position',
            field=models.CharField(blank=True, choices=[('CEO', 'CEO'), ('Chief Finance Officer', 'Chief Finance Officer'), ('Senior Operation Manager', 'Senior Operation Manager'), ('Operation Manager', 'Operation Manager'), ('Admin Manager', 'Admin Manager'), ('Senior Operation Manager', 'Senior Operation Manager'), ('Project Manager', 'Project Manager'), ('Team Lead', 'Team Lead'), ('General Administrative Support', 'General Administrative Support'), ('Executive Assistant to CEO', 'Executive Assistant to CEO'), ('Human Resource Specialist', 'Human Resource Specialist'), ('Recruitment Specialist', 'Recruitment Specialist'), ('IT Manager', 'IT Manager'), ('IT Support', 'IT Support'), ('Customer Support', 'Customer Support')], max_length=150, null=True),
        ),
    ]
