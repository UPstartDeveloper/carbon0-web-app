# Generated by Django 3.1.1 on 2021-03-17 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carbon_quiz", "0098_question_is_quiz_question"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mission",
            name="priority_level",
            field=models.IntegerField(
                choices=[
                    (0, "Beginner Level"),
                    (1, "Intermediate Level"),
                    (2, "Advanced Level"),
                    (3, "Expert Level"),
                ],
                default=0,
                help_text="The stage at which a player is ready for this mission.",
            ),
        ),
    ]