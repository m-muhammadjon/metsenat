# Generated by Django 4.1.3 on 2022-11-21 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='type',
            field=models.CharField(choices=[('natural_person', 'Natural person'), ('legal_entity', 'Legal entity')], max_length=255),
        ),
    ]