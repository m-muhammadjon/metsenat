from rest_framework import serializers

from main import models


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sponsor
        fields = '__all__'

    # def create(self, validated_data):
    #     print(validated_data)
    #     print(not validated_data.get('organization_name'))
    #     if validated_data.get('type') == 'legal_entity' and not validated_data.get('organization_name'):
    #         print('***')
    #     sponsor_req = super().create(validated_data)
    #     sponsor_req.save()
    #     return sponsor_req
