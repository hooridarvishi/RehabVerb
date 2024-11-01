# Generated by Django 5.1.2 on 2024-10-31 22:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("verbtherapy", "0002_texttemplate"),
    ]

    operations = [
        migrations.AddField(
            model_name="card",
            name="adverb",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="card",
            name="pre_adverb",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="card",
            name="pre_position",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="card",
            name="subject",
            field=models.CharField(blank=True, max_length=320, null=True),
        ),
        migrations.AddField(
            model_name="card",
            name="text_mafool",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]