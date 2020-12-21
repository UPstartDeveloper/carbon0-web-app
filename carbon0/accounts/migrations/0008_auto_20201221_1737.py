# Generated by Django 3.1.1 on 2020-12-21 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201211_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='diet_sign_photo',
            field=models.ImageField(blank=True, help_text="User's sign for their Diet Missions.", null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='offsets_sign_photo',
            field=models.ImageField(blank=True, help_text="User's sign for their Airline-Utilities Missions.", null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='recycling_sign_photo',
            field=models.ImageField(blank=True, help_text="User's sign for their Recycling Missions.", null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='transit_sign_photo',
            field=models.ImageField(blank=True, help_text="User's sign for their Transit Missions.", null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='utilities_sign_photo',
            field=models.ImageField(blank=True, help_text="User's sign for their Utilities Missions.", null=True, upload_to='images/'),
        ),
    ]
