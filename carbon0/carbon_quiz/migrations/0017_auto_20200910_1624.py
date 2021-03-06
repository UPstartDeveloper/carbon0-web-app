# Generated by Django 3.1.1 on 2020-09-10 20:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carbon_quiz", "0016_auto_20200910_1623"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quiz",
            name="questions",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.IntegerField(),
                blank=True,
                help_text="Array of ids for the quiz questions.",
                null=True,
                size=5,
            ),
        ),
    ]
