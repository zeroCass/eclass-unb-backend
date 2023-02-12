# Generated by Django 3.2.17 on 2023-02-12 02:11

from django.db import migrations #type: ignore


class Migration(migrations.Migration):

    dependencies = [
        ('e_class', '0020_discursivequestion_question_multiplequestion_exams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exams',
            name='discursiveQuestions',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='multipleQuestions',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='students',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='multiplequestion',
            name='question_ptr',
        ),
        migrations.RemoveField(
            model_name='question',
            name='students',
        ),
        migrations.RemoveField(
            model_name='question',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='DiscursiveQuestion',
        ),
        migrations.DeleteModel(
            name='Exams',
        ),
        migrations.DeleteModel(
            name='MultipleQuestion',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
