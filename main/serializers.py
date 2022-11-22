from rest_framework import serializers

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


class SponsorDailyStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SponsorDailyStat
        exclude = ['id']


class StudentDailyStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentDailyStat
        exclude = ['id']


class DashboardSerializer(serializers.ModelSerializer):
    sponsor_chart = serializers.SerializerMethodField()
    student_chart = serializers.SerializerMethodField()

    class Meta:
        model = models.Dashboard
        exclude = ['id']

    def get_sponsor_chart(self, obj):
        return SponsorDailyStatSerializer(models.SponsorDailyStat.objects.all().order_by('date'), many=True).data

    def get_student_chart(self, obj):
        return SponsorDailyStatSerializer(models.StudentDailyStat.objects.all().order_by('date'), many=True).data
