# Generated by Django 2.2.7 on 2019-11-19 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teams', '0003_auto_20191119_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='group_photo',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
