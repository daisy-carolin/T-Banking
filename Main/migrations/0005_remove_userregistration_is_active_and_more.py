# Generated by Django 4.2.4 on 2023-08-28 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_remove_contribution_fine_details_contribution_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregistration',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='userregistration',
            name='is_staff',
        ),
    ]
