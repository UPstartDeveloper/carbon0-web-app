# Generated by Django 3.1.1 on 2020-10-07 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_users_footprint'),
        ('carbon_quiz', '0055_achievement_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='profile',
            field=models.ForeignKey(help_text='The profile that owns this achievement.', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]
