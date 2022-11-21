from django.db import models

from main import validators


class Sponsor(models.Model):
    class TYPE_CHOICES(models.TextChoices):
        natural_person = ('natural_person', 'Natural person')
        legal_entity = ('legal_entity', 'Legal entity')

    class PRICE_CHOICES(models.IntegerChoices):
        one_mln = 1000000
        five_mln = 5000000
        seven_mln = 7000000
        ten_mln = 10000000
        thirty_mln = 30000000
        other = 0

    type = models.CharField(max_length=255, choices=TYPE_CHOICES.choices)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, validators=[validators.phone_number_validator])
    payment_amount = models.IntegerField(choices=PRICE_CHOICES.choices)
    other_price = models.PositiveBigIntegerField(null=True, blank=True)
    organization_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.full_name}'
