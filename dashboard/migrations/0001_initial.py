# Generated by Django 4.1.7 on 2023-03-15 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Crane",
            fields=[
                ("id", models.SmallAutoField(primary_key=True, serialize=False)),
                ("reg_no", models.CharField(max_length=54)),
                (
                    "image",
                    models.ImageField(
                        default="images/default.jfif", upload_to="images/"
                    ),
                ),
                ("about", models.TextField()),
                (
                    "design_capacity",
                    models.CharField(
                        choices=[
                            ("10 Ton", "10 Ton"),
                            ("20 Ton", "20 Ton"),
                            ("30 Ton", "30 Ton"),
                            ("40 Ton", "40 Ton"),
                            ("60 Ton", "60 Ton"),
                            ("80 Ton", "80 Ton"),
                            ("100 Ton", "100 Ton"),
                            ("130 Ton", "130 Ton"),
                            ("160 Ton", "160 Ton"),
                            ("250 Ton", "250 Ton"),
                        ],
                        max_length=54,
                    ),
                ),
                (
                    "availability",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")], max_length=54
                    ),
                ),
                (
                    "fault_type",
                    models.CharField(
                        choices=[
                            ("Corrective", "Corrective"),
                            ("Servicing", "Servicing"),
                            ("Unavailable", "Unavailable"),
                            ("Not Specified", "Not Specified"),
                            ("None", "None"),
                        ],
                        max_length=54,
                    ),
                ),
                (
                    "remark",
                    models.CharField(
                        choices=[
                            ("Awaiting Spare", "Awaiting Spare"),
                            ("In progress", "In Progress"),
                            ("Good Condition", "Good Condition"),
                            ("Breakdown", "Breakdown"),
                            ("None", "None"),
                        ],
                        max_length=54,
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="CraneLatestUpdate",
            fields=[
                ("id", models.SmallAutoField(primary_key=True, serialize=False)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[("Apply Update", "Apply Updated Time")],
                        max_length=55,
                        null=True,
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Crane Update",
                "verbose_name_plural": "Apply Updates",
            },
        ),
        migrations.CreateModel(
            name="CraneModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
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
                ("description", models.TextField()),
            ],
            options={
                "verbose_name": "Crane Categories",
                "verbose_name_plural": "Crane Categories",
            },
        ),
        migrations.CreateModel(
            name="Job",
            fields=[
                ("id", models.SmallAutoField(primary_key=True, serialize=False)),
                ("job_num", models.CharField(max_length=54)),
                ("job_description", models.TextField()),
                ("start_date", models.DateTimeField(auto_now=True)),
                ("end_date", models.DateTimeField(auto_now_add=True)),
                (
                    "crane",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.crane",
                    ),
                ),
            ],
            options={
                "verbose_name": "Associated Jobs",
                "verbose_name_plural": "Associated Jobs",
            },
        ),
        migrations.AddField(
            model_name="crane",
            name="name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dashboard.cranemodel"
            ),
        ),
    ]