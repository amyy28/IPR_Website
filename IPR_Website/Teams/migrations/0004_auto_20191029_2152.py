# Generated by Django 2.1.3 on 2019-10-29 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teams', '0003_auto_20191029_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teams',
            old_name='member_1',
            new_name='member_1_name',
        ),
        migrations.RenameField(
            model_name='teams',
            old_name='member_2',
            new_name='member_2_name',
        ),
        migrations.RenameField(
            model_name='teams',
            old_name='member_3',
            new_name='member_2_usn',
        ),
        migrations.AddField(
            model_name='teams',
            name='member_1_usn',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teams',
            name='member_3_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
