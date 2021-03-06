# Generated by Django 3.1.1 on 2020-09-09 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carbon_quiz", "0007_mission_learn_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mission",
            name="completion_date",
        ),
        migrations.AddField(
            model_name="achievement",
            name="completion_date",
            field=models.DateTimeField(
                blank=True, help_text="Date mission was accomplished", null=True
            ),
        ),
    ]
