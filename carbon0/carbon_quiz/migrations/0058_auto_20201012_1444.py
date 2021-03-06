# Generated by Django 3.1.1 on 2020-10-12 18:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carbon_quiz", "0057_auto_20201008_1209"),
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
                            "assets/glb-files/CarrotWithFace.glb",
                            "assets/usdz-files/tree.usdz",
                        ],
                        "Nature's Model",
                    ),
                    (["assets/glb-files/Wheel.glb", "None"], "Wheel Model"),
                    (
                        ["assets/glb-files/Bin.glb", "assets/usdz-files/bin.usdz"],
                        "Bin Model",
                    ),
                    (
                        ["assets/glb-files/coin.glb", "assets/usdz-files/coin.usdz"],
                        "Coin Model",
                    ),
                    (
                        [
                            "assets/glb-files/Light bulb 1.glb",
                            "assets/usdz-files/Lightbulb.usdz",
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
