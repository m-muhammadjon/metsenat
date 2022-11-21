from rest_framework import generics, status
from rest_framework.response import Response

from main import models, serializers


class SponsorView(generics.ListCreateAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorSerializer

    def post(self, request, *args, **kwargs):
        serializer = serializers.SponsorSerializer(data=request.data)
        if serializer.is_valid():
            if request.data.get('type') == 'legal_entity' and not request.data.get('organization_name'):
                return Response({'success': False, 'message': 'Organization name is required'},
                                status=status.HTTP_400_BAD_REQUEST)
            print(request.data.get('payment_amount'))
            if request.data.get('payment_amount') == '0' and not request.data.get('other_price'):
                return Response({'success': False, 'message': 'Other price is required'},
                                status=status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)
