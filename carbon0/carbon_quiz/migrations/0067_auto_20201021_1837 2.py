# Generated by Django 3.1.1 on 2020-10-21 22:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carbon_quiz", "0066_merge_20201021_1837"),
    ]

    operations = [
        migrations.AlterField(
            model_name="achievement",
            name="zeron_image_url",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(blank=True, max_length=100, null=True),
                blank=True,
                choices=[
                    (
                        [
                            "assets/glb-files/carrot2.glb",
                            "assets/usdz-files/carrot2.usdz",
                        ],
                        "Nature's Model",
                    ),
                    (
                        [
                            "assets/glb-files/wheel2.glb",
                            "assets/usdz-files/wheel2.usdz",
                        ],
                        "Wheel Model",
                    ),
                    (
                        ["assets/glb-files/Bin2.glb", "assets/usdz-files/Bin2.usdz"],
                        "Bin Model",
                    ),
                    (
                        ["assets/glb-files/Coin2.glb", "assets/usdz-files/Coin2.usdz"],
                        "Coin Model",
                    ),
                    (
                        [
                            "assets/glb-files/lightbulb2.glb",
                            "assets/usdz-files/lightbulb2.usdz",
                        ],
                        "Light Bulb Model",
                    ),
                ],
                help_text="File paths to the 3D model in storage.",
                null=True,
                size=None,
            ),
        ),
    ]
