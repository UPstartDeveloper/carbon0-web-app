# Generated by Django 3.1.1 on 2020-09-10 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carbon_quiz', '0017_auto_20200910_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='mission',
            field=models.ForeignKey(help_text='The mission that earns this achievement.', null=True, on_delete=django.db.models.deletion.PROTECT, to='carbon_quiz.mission'),
        ),
    ]