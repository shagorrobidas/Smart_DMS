from rest_framework import serializers

from Document.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'id',
            'name',
            'code',
            'short_name'
        )