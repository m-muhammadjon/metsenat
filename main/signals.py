from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import Donation


@receiver(post_save, sender=Donation)
def donation_created(sender, instance, created, **kwargs):
    if created:
        student = instance.student
        sponsor = instance.sponsor
        student.allocated_amount += instance.amount
        student.save()
        sponsor.amount_spent += instance.amount
        sponsor.save()
