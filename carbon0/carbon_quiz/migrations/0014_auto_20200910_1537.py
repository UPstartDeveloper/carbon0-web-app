# Generated by Django 3.1.1 on 2020-09-10 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carbon_quiz", "0013_question_learn_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quiz",
            name="active_question",
            field=models.IntegerField(
                blank=True,
                default=-1,
                help_text="Id of the question currently being asked.",
            ),
        ),
    ]
