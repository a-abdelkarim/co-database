# Generated by Django 3.2 on 2023-05-16 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20230516_2032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='country',
            new_name='country_id',
        ),
    ]