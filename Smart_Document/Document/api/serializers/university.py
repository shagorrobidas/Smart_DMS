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