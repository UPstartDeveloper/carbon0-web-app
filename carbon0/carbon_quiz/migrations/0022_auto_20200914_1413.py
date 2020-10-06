# Generated by Django 3.1.1 on 2020-09-14 18:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbon_quiz', '0021_auto_20200912_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='symbol',
            field=models.ImageField(blank=True, help_text='Visual associated to action user takes.', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='questions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, help_text='Array of ids for the quiz questions.', null=True, size=5),
        ),
    ]