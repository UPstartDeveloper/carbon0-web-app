# Generated by Django 3.1.1 on 2021-02-12 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Plant",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nickname",
                    models.CharField(
                        help_text="What do you call this plant?", max_length=5000
                    ),
                ),
                (
                    "common_name",
                    models.CharField(
                        blank=True,
                        help_text="What species is this plant, if you know?",
                        max_length=5000,
                        null=True,
                    ),
                ),
                (
                    "is_edible",
                    models.BooleanField(
                        default=False,
                        help_text="Are you growing this plant to grow your own food?",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Please share anything else you'd like to add about what             condition your plant is in (because we care)!",
                        null=True,
                    ),
                ),
            ],
        ),
    ]
