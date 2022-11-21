# Generated by Django 4.1.3 on 2022-11-21 08:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Natural person', 'Natural person'), ('Legal entity', 'Legal entity')], max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Invalid phone number', regex='^[\\+]?[(]?[0-9]{5}[)]?[-\\s\\.]?[0-9]{3}[-\\s\\.]?[0-9]{2}[-\\s\\.]?[0-9]{2}$')])),
                ('payment_amount', models.IntegerField(choices=[(1000000, 'One Mln'), (5000000, 'Five Mln'), (7000000, 'Seven Mln'), (10000000, 'Ten Mln'), (30000000, 'Thirty Mln'), (0, 'Other')])),
                ('other_price', models.PositiveBigIntegerField(blank=True, null=True)),
                ('organization_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
