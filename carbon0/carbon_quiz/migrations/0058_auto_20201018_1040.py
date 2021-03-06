# Generated by Django 3.1.1 on 2020-10-18 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carbon_quiz", "0057_auto_20201008_1209"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quiz",
            name="carbon_value_total",
            field=models.FloatField(
                blank=True,
                default=1000,
                help_text="Total metric tons of carbon that the user can eliminate.",
            ),
        ),
    ]
