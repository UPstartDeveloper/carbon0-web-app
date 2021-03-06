# Generated by Django 3.1.1 on 2020-09-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carbon_quiz", "0012_auto_20200909_2136"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="learn_image",
            field=models.ImageField(
                blank=True,
                help_text="Symbolizes what user needs to work on.",
                null=True,
                upload_to="images/",
            ),
        ),
    ]
