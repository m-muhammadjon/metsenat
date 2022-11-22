from django_filters import rest_framework as filters

from main import models


class SponsorFilter(filters.FilterSet):
    payment_amount = filters.NumberFilter(field_name='payment_amount', lookup_expr='lte')

    class Meta:
        model = models.Sponsor
        fields = ['status', 'payment_amount', 'created_at']


class StudentFilter(filters.FilterSet):
    class Meta:
        model = models.Student
        fields = ['degree', 'university']
