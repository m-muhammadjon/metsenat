from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from main import models


@receiver(post_save, sender=models.Donation)
def donation_created(sender, instance, created, **kwargs):
    if created:
        student = instance.student
        sponsor = instance.sponsor
        student.allocated_amount += instance.amount
        student.save()
        sponsor.amount_spent += instance.amount
        sponsor.save()
        dashboard = models.Dashboard.objects.first()
        dashboard.amount_paid += instance.amount
        dashboard.amount_due -= instance.amount
        dashboard.save()


@receiver(post_save, sender=models.Sponsor)
def sponsor_created(sender, instance, created, **kwargs):
    if created:
        dashboard = models.Dashboard.objects.first()
        dashboard.sponsors_count += 1
        dashboard.save()
        obj, is_created = models.SponsorDailyStat.objects.get_or_create(date=timezone.now())
        obj.count = dashboard.sponsors_count
        obj.save()


@receiver(post_save, sender=models.Student)
def student_created(sender, instance, created, **kwargs):
    if created:
        dashboard = models.Dashboard.objects.first()
        dashboard.students_count += 1
        dashboard.amount_requested += instance.required_amount
        dashboard.amount_due += instance.required_amount
        dashboard.save()
        obj, is_created = models.StudentDailyStat.objects.get_or_create(date=timezone.now())
        obj.count = dashboard.students_count
        obj.save()
