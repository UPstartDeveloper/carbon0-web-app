# Generated by Django 3.1.1 on 2021-02-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("garden", "0002_auto_20210214_1344"),
    ]

    operations = [
        migrations.AddField(
            model_name="leaf",
            name="condition",
            field=models.CharField(
                help_text="What the AI identified on the leaf.",
                max_length=100,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="leaf",
            name="confidence",
            field=models.FloatField(
                default=0.02631578947368421,
                help_text="How confident the AI was in its prediction.",
            ),
        ),
        migrations.AddField(
            model_name="leaf",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Image of the leaf.",
                null=True,
                upload_to="images/",
            ),
        ),
        migrations.AddField(
            model_name="leaf",
            name="status",
            field=models.CharField(
                choices=[("H", "Heathy"), ("U", "Unhealthy"), ("M", "Moderate")],
                default="M",
                help_text="The healthiness of this leaf.",
                max_length=1,
            ),
        ),
    ]
