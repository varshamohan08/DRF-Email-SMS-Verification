# Generated by Django 5.0.3 on 2024-03-17 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationform_app', '0003_userdetails_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
