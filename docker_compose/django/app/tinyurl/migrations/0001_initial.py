# Generated by Django 4.0.6 on 2022-07-10 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TinyUrl",
            fields=[
                (
                    "short_url",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("original_url", models.CharField(max_length=100)),
            ],
        ),
    ]
