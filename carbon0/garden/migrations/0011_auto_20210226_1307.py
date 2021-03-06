# Generated by Django 3.1.1 on 2021-02-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("garden", "0010_auto_20210225_1017"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plant",
            name="is_edible",
            field=models.BooleanField(
                default=False,
                help_text="Are you growing this plant to grow your own food?",
                null=True,
            ),
        ),
    ]
