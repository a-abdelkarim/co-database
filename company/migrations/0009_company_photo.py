# Generated by Django 3.2 on 2023-05-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_auto_20230527_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='photo',
            field=models.ImageField(default='images/no_image.png', upload_to='images/company/'),
        ),
    ]