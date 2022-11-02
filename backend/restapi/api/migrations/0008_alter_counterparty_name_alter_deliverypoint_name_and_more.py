# Generated by Django 4.1.3 on 2022-11-02 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_rename_cp_name_counterparty_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="counterparty",
            name="name",
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="deliverypoint",
            name="name",
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="tool",
            name="name",
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="type",
            name="name",
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]
