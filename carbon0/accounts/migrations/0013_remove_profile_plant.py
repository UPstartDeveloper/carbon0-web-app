# Generated by Django 3.1.1 on 2021-02-15 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0012_profile_plant"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="plant",
        ),
    ]
