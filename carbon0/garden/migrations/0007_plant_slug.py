# Generated by Django 3.1.1 on 2021-02-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("garden", "0006_plant_created"),
    ]

    operations = [
        migrations.AddField(
            model_name="plant",
            name="slug",
            field=models.CharField(
                blank=True,
                help_text="Unique parameter to specify the Plant in the URL path.",
                max_length=500,
                null=True,
                unique=True,
            ),
        ),
    ]
