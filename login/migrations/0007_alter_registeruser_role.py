# Generated by Django 4.0.7 on 2022-10-22 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_registeruser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeruser',
            name='role',
            field=models.CharField(choices=[('Patient', 'Patient'), ('Doctor', 'Doctor')], default='1', max_length=200),
        ),
    ]
