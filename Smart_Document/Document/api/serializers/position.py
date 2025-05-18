from rest_framework import serializers
from Document.models import Position


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = (
            'id',
            'title',
            'position_code',
        )