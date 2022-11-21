from django.db import models

from main import validators


class Sponsor(models.Model):
    class STATUS_CHOICES(models.TextChoices):
        new = ('new', 'New')
        in_moderation = ('in_moderation', 'In moderation')
        approved = ('approved', 'Approved')
        cancelled = ('cancelled', 'Cancelled')

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

    status = models.CharField(max_length=255, choices=STATUS_CHOICES.choices, default=STATUS_CHOICES.in_moderation)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES.choices)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, validators=[validators.phone_number_validator])
    payment_amount = models.BigIntegerField(choices=PRICE_CHOICES.choices)
    other_payment = models.BigIntegerField(null=True, blank=True)
    amount_spent = models.BigIntegerField(default=0, blank=True)
    organization_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name}'

    def save(self, *args, **kwargs):
        if self.type == 'legal_entity' and not self.organization_name:
            raise ValueError('Invalid organisation name')
        if self.payment_amount == 0 and not self.other_payment:
            raise ValueError('Invalid other price')
        super(Sponsor, self).save(*args, **kwargs)

    def get_total_payment_amount(self):
        return self.payment_amount or self.other_payment


class University(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'


class Student(models.Model):
    class DEGREE_CHOICES(models.TextChoices):
        bachelor = ('bachelor', 'Bachelor')
        master = ('master', 'Master')

    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, validators=[validators.phone_number_validator])
    university = models.ForeignKey(University,
                                   on_delete=models.SET_NULL,
                                   related_name='students',
                                   null=True)
    required_amount = models.PositiveIntegerField()
    allocated_amount = models.PositiveIntegerField(default=0, blank=True)
    sponsors = models.ManyToManyField(Sponsor,
                                      related_name='sponsored_students',
                                      blank=True)

    def __str__(self):
        return f'student {self.full_name}'
