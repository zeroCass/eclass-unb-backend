# Generated by Django 4.1.6 on 2023-02-12 17:48

from django.db import migrations, models #type: ignore


class Migration(migrations.Migration):
    dependencies = [
        ("e_class", "0023_alter_classes_endtime_alter_classes_starttime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="classes",
            name="endTime",
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name="classes",
            name="startTime",
            field=models.DateTimeField(blank=True),
        ),
    ]
