# Generated by Django 4.2.4 on 2023-08-25 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_member_group_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='group_id',
            new_name='group',
        ),
    ]
