# Generated by Django 3.1.1 on 2020-09-14 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carbon_quiz', '0022_auto_20200914_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mission',
            name='symbol',
        ),
    ]