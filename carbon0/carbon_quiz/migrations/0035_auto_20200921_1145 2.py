# Generated by Django 3.1.1 on 2020-09-21 15:45

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carbon_quiz", "0034_auto_20200921_1143"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mission",
            name="links",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=django.contrib.postgres.fields.ArrayField(
                    base_field=models.CharField(blank=True, max_length=100, null=True),
                    help_text="Links the user can click to complete the mission.",
                    null=True,
                    size=2,
                ),
                null=True,
                size=3,
            ),
        ),
    ]
