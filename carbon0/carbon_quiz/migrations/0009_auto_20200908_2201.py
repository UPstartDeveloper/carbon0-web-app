# Generated by Django 3.1.1 on 2020-09-09 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("carbon_quiz", "0008_auto_20200908_2142"),
    ]

    operations = [
        migrations.AddField(
            model_name="achievement",
            name="badge_name",
            field=models.CharField(
                blank=True,
                help_text="The badge that the user earns in this achievement.",
                max_length=200,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="achievement",
            name="mission",
            field=models.OneToOneField(
                help_text="The mission that earns this achievement.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="carbon_quiz.mission",
            ),
        ),
        migrations.AddField(
            model_name="achievement",
            name="user",
            field=models.ForeignKey(
                help_text="The user who completed the mission.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="achievement",
            name="zeron_image",
            field=models.FileField(
                blank=True,
                help_text="To be revisited in Feature 2.",
                null=True,
                upload_to="",
            ),
        ),
        migrations.AddField(
            model_name="achievement",
            name="zeron_name",
            field=models.CharField(default="Zeron prize", max_length=200),
        ),
    ]
