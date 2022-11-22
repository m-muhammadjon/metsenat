from rest_framework import serializers, status
from rest_framework.response import Response

from main import models


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sponsor
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.University
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    university = serializers.SerializerMethodField()

    class Meta:
        model = models.Student
        fields = '__all__'

    def get_university(self, obj):
        return UniversitySerializer(obj.university).data

    def create(self, validated_data):
        university_id = int(self.context['request'].data.get('university'))
        try:
            university = models.University.objects.get(id=university_id)
            validated_data['university'] = university
        except models.University.DoesNotExist:
            raise serializers.ValidationError({'success': False, 'message': 'An unexpected error occurred'})
        student = super().create(validated_data)
        student.save()
        return student


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Donation
        fields = '__all__'
