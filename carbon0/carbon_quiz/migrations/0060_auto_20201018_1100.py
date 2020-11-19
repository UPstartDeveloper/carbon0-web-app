# Generated by Django 3.1.1 on 2020-10-18 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carbon_quiz", "0059_question_good_response"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="good_response",
        ),
        migrations.AddField(
            model_name="question",
            name="improvement_response",
            field=models.IntegerField(
                choices=[(1, "Yes"), (0, "No")],
                default=1,
                help_text="Response that says the user needs to improve, with regards to this area of their carbon footprint.",
            ),
        ),
    ]
