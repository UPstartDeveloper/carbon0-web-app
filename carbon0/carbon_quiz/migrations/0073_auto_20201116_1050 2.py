# Generated by Django 3.1.1 on 2020-11-16 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbon_quiz', '0072_auto_20201104_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True, help_text="User's response.", null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='is_open_response',
            field=models.BooleanField(default=False, help_text='Is the question answered with text or not.'),
        ),
        migrations.AlterField(
            model_name='question',
            name='improvement_response',
            field=models.IntegerField(choices=[(1, 'Yes'), (0, 'No'), (-1, 'Open-Response')], default=0, help_text='Response that says the user needs to improve, with regards to this area of their carbon footprint.'),
        ),
    ]
