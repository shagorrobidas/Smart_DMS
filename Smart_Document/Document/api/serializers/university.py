from rest_framework import serializers
from Document.models import University


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = (
            'id',
            'name',
            'logo',
            'code',
            'location',
        )

        def create(self, validated_data):
            logo = validated_data.pop('logo', None)
            instance = University.objects.create(**validated_data)
            if logo:
                instance.logo = logo
                instance.save()
            return instance
