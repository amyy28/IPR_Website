# Generated by Django 2.1.3 on 2019-10-13 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_group_number', models.IntegerField()),
                ('team_member_1', models.CharField(max_length=100)),
                ('team_member_2', models.CharField(max_length=100)),
                ('team_member_3', models.CharField(max_length=100)),
                ('team_usn_1', models.CharField(max_length=100)),
                ('team_usn_2', models.CharField(max_length=100)),
                ('team_usn_3', models.CharField(max_length=100)),
            ],
        ),
    ]