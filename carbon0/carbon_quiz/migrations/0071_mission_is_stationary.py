# Generated by Django 3.1.1 on 2020-11-03 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbon_quiz', '0070_auto_20201027_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='is_stationary',
            field=models.BooleanField(default=False, help_text='Would the player get off the couch to complete this?'),
        ),
    ]
