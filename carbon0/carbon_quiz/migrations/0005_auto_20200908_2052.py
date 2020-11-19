# Generated by Django 3.1.1 on 2020-09-09 00:52

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("carbon_quiz", "0004_auto_20200908_2037"),
    ]

    operations = [
        migrations.AddField(
            model_name="mission",
            name="description",
            field=models.TextField(
                blank=True, help_text="Explains the details of the mission.", null=True
            ),
        ),
        migrations.AddField(
            model_name="mission",
            name="links",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=500),
                blank=True,
                help_text="Links that the user can click to complete the mission.",
                null=True,
                size=3,
            ),
        ),
        migrations.AddField(
            model_name="mission",
            name="question",
            field=models.ForeignKey(
                help_text="The question to which this mission relates.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="carbon_quiz.question",
            ),
        ),
        migrations.AddField(
            model_name="mission",
            name="status",
            field=models.BooleanField(
                default=False, help_text="If the mission is done or not."
            ),
        ),
        migrations.AddField(
            model_name="mission",
            name="title",
            field=models.CharField(
                help_text="Title of the mission.",
                max_length=500,
                null=True,
                unique=True,
            ),
        ),
    ]
