# Generated by Django 4.1 on 2022-12-05 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submit", "0001_initial"),
    ]

    operations = [
        migrations.RemoveConstraint(model_name="class", name="Class-unique",),
        migrations.RenameField(
            model_name="class", old_name="preiod", new_name="period",
        ),
        migrations.AddConstraint(
            model_name="class",
            constraint=models.UniqueConstraint(
                fields=("day", "period", "ID"), name="Class-unique"
            ),
        ),
    ]