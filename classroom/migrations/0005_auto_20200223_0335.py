# Generated by Django 2.2.3 on 2020-02-23 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_quiz_quizno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='quizno',
            new_name='quiz_no',
        ),
    ]
