# Generated by Django 4.1.7 on 2023-09-29 10:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0006_crane_purchase_date_alter_crane_fault_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="crane",
            name="fault_type",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="crane",
            name="remark",
            field=models.CharField(max_length=255),
        ),
    ]
