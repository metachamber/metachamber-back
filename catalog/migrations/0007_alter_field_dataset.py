# Generated by Django 4.0.6 on 2022-10-13 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_field_delete_datafield_alter_dataset_datasource_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='dataset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fields', to='catalog.dataset', verbose_name='Dataset'),
        ),
    ]
