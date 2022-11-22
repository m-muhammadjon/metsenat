from django.contrib import admin

from main import models

admin.site.register(models.Sponsor)
admin.site.register(models.University)
admin.site.register(models.Student)
admin.site.register(models.Donation)
admin.site.register(models.SponsorDailyStat)
admin.site.register(models.StudentDailyStat)


@admin.register(models.Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return models.Dashboard.objects.count() < 1

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
