# Generated by Django 3.2 on 2023-05-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_alter_company_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='photo',
            field=models.ImageField(default='images/no_image.png', upload_to='images/company/'),
        ),
    ]
