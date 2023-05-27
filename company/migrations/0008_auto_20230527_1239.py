# Generated by Django 3.2 on 2023-05-27 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_company_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='company',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
    ]