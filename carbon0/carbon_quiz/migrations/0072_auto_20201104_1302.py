# Generated by Django 3.1.1 on 2020-11-04 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbon_quiz', '0071_mission_is_stationary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='is_stationary',
            field=models.BooleanField(default=False, help_text='Does the player need to get off the couch to complete this?'),
        ),
    ]