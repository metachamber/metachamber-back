# Generated by Django 4.0.6 on 2022-07-15 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_dataset_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataset",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Description"),
        ),
        migrations.AlterField(
            model_name="datasource",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Description"),
        ),
    ]
