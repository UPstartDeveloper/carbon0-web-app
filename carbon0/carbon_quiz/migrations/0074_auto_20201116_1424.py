# Generated by Django 3.1.1 on 2020-11-16 19:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbon_quiz', '0073_auto_20201116_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='is_open_response',
        ),
        migrations.AddField(
            model_name='quiz',
            name='open_response_answers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, help_text="User's response.", null=True), blank=True, null=True, size=None),
        ),
    ]