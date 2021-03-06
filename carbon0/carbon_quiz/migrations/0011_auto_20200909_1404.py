# Generated by Django 3.1.1 on 2020-09-09 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("carbon_quiz", "0010_auto_20200909_0853"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mission",
            name="question",
            field=models.ForeignKey(
                help_text="The question to which this mission relates.",
                on_delete=django.db.models.deletion.PROTECT,
                to="carbon_quiz.question",
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="slug",
            field=models.SlugField(
                blank=True,
                editable=False,
                help_text="Unique URL path to access this quiz. Generated by the system.",
                max_length=500,
                null=True,
            ),
        ),
    ]
