# Generated by Django 4.1.3 on 2022-11-21 17:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Invalid phone number', regex='^[\\+]?[(]?[0-9]{5}[)]?[-\\s\\.]?[0-9]{3}[-\\s\\.]?[0-9]{2}[-\\s\\.]?[0-9]{2}$')])),
                ('required_amount', models.PositiveIntegerField()),
                ('allocated_amount', models.PositiveIntegerField(default=0)),
                ('sponsors', models.ManyToManyField(related_name='sponsored_students', to='main.sponsor')),
                ('university', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='main.university')),
            ],
        ),
    ]
