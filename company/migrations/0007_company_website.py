# Generated by Django 3.2 on 2023-05-16 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20230516_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.CharField(default='www.xxxxx.com', max_length=255),
            preserve_default=False,
        ),
    ]
