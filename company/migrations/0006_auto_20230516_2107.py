# Generated by Django 3.2 on 2023-05-16 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_rename_country_company_country_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='country_id',
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.CharField(default='مصر', max_length=255),
            preserve_default=False,
        ),
    ]
