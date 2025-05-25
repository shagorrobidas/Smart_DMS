from rest_framework import serializers
from Document.models import University


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = (
            'id',
            'name',
            'logo_path',
            'university_code',
            'location',
        )

        def create(self, validated_data):
            logo = validated_data.pop('logo_path', None)
            instance = University.objects.create(**validated_data)
            if logo:
                instance.logo_path = logo
                instance.save()
            return instance
