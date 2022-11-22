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


class UniversityView(generics.ListAPIView):
    queryset = models.University.objects.all()
    serializer_class = serializers.UniversitySerializer


class StudentView(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    filter_backends = [drf_filters.DjangoFilterBackend]
    filterset_class = filters.StudentFilter

    def post(self, request, *args, **kwargs):
        if not request.data.get('university'):
            return Response({"university": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class DonationView(generics.ListCreateAPIView):
    queryset = models.Donation.objects.all()
    serializer_class = serializers.DonationSerializer

    def post(self, request, *args, **kwargs):
        errors = [i if not i in request.data else -1 for i in ['sponsor', 'student', 'amount']]
        print(errors)
        error_message = {}
        for error in errors:
            if error != -1:
                error_message[error] = ['This field is required.']
        if errors.count(-1) != 3:
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
        student = models.Student.objects.filter(id=int(request.data.get('student'))).first()
        sponsor = models.Sponsor.objects.filter(id=int(request.data.get('sponsor'))).first()
        money = int(request.data.get('amount'))
        if student.clean_money(money) and sponsor.enough_money(money):
            return self.create(request, *args, **kwargs)
        elif student.earned():
            return Response(
                {'success': False, 'message': f'Student already earned enough money you do not need to add sponsor'},
                status=status.HTTP_400_BAD_REQUEST)

        elif not student.clean_money(money):
            return Response(
                {'success': False,
                 'message': f'Given money is too much for student.\nSuggested money {student.required_amount - student.allocated_amount}'},
                status=status.HTTP_400_BAD_REQUEST)
        elif sponsor.rest_of_money() == 0:
            return Response(
                {'success': False,
                 'message': f'Sponsor\'s money do not leave'},
                status=status.HTTP_400_BAD_REQUEST)
        elif not sponsor.enough_money(money):
            return Response(
                {'success': False,
                 'message': f'Sponsor\s money is not enough.\nSuggested money {min(student.required_amount - student.allocated_amount, sponsor.rest_of_money())}'},
                status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': False, 'message': 'An unexpected error occurred'},
                        status=status.HTTP_400_BAD_REQUEST)


class DashboardView(generics.ListAPIView):
    queryset = models.Dashboard.objects.all()
    serializer_class = serializers.DashboardSerializer
