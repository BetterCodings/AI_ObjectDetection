# Generated by Django 4.1 on 2022-12-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submit", "0005_rename_lid_class_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="class", name="day", field=models.IntegerField(default=0),
        ),
    ]