# Generated by Django 4.2 on 2023-04-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dash", "0003_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="song",
            name="audio_file",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
    ]
