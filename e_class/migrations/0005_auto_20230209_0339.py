# Generated by Django 3.2.17 on 2023-02-09 06:39

from django.db import migrations, models #type:ignore
import django.db.models.deletion #type:ignore


class Migration(migrations.Migration):

    dependencies = [
        ('e_class', '0004_auto_20230209_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='Users_registrationID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='e_class.users'),
        ),
    ]
