# Generated by Django 3.2 on 2023-05-16 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='e@cmo.com', max_length=254),
            preserve_default=False,
        ),
    ]
