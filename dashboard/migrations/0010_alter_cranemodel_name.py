# Generated by Django 4.1.7 on 2023-09-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0009_alter_crane_design_capacity_alter_cranemodel_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cranemodel",
            name="name",
            field=models.CharField(
                choices=[
                    ("Terex Crane", "Terex Crane"),
                    ("Grove Crane", "Grove Crane"),
                    ("Locatelli Crane", "Locatelli Crane"),
                    ("Grove Yard Boss Crane", "Grove Yard Boss Crane"),
                    ("Grove Rough Terrain", "Grove Rough Terrain"),
                ],
                max_length=54,
            ),
        ),
    ]