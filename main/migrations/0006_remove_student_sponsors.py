# Generated by Django 4.1.3 on 2022-11-22 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_student_university'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='sponsors',
        ),
    ]