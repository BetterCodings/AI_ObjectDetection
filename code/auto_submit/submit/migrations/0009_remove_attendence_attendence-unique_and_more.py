# Generated by Django 4.1 on 2022-12-06 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("submit", "0008_remove_attendence_attendence-unique_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(model_name="attendence", name="Attendence-unique",),
        migrations.RemoveField(model_name="attendence", name="image",),
    ]
