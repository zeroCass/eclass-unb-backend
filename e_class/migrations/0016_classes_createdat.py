# Generated by Django 4.1.6 on 2023-02-11 04:07

from django.db import migrations, models #type: ignore
import django.utils.timezone #type: ignore


class Migration(migrations.Migration):
    dependencies = [
        ("e_class", "0015_classes_rename_admin_id_subject_admin_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="classes",
            name="createdAt",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
