# Generated by Django 3.1.1 on 2020-09-12 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("carbon_quiz", "0019_quiz_current_question_answered_yes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="quiz",
            name="current_question_answered_yes",
        ),
    ]
