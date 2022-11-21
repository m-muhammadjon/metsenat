from django_filters import rest_framework as drf_filters
from rest_framework import generics, status
from rest_framework.response import Response

from main import models, serializers, filters


class SponsorView(generics.ListCreateAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorSerializer
    filter_backends = (drf_filters.DjangoFilterBackend,)
    filterset_class = filters.SponsorFilter

    def post(self, request, *args, **kwargs):
        serializer = serializers.SponsorSerializer(data=request.data)
        if serializer.is_valid():
            if request.data.get('type') == 'legal_entity' and not request.data.get('organization_name'):
                return Response({'success': False, 'message': 'Organization name is required'},
                                status=status.HTTP_400_BAD_REQUEST)
            if request.data.get('payment_amount') == '0' and not request.data.get('other_payment'):
                return Response({'success': False, 'message': 'Other price is required'},
                                status=status.HTTP_400_BAD_REQUEST)
            if request.data.get('type') == 'natural_person' and request.data.get('organization_name'):
                return Response({'success': False, 'message': 'An unexpected error occurred'},
                                status=status.HTTP_400_BAD_REQUEST)
            if not request.data.get('payment_amount') == '0' and request.data.get('other_payment'):
                return Response({'success': False, 'message': 'An unexpected error occurred'},
                                status=status.HTTP_400_BAD_REQUEST)

        return self.create(request, *args, **kwargs)


class SponsorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorSerializer
