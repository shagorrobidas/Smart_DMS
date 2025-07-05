from rest_framework import serializers
from Document.models import Program


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = (
            'id',
            'program_name',
            'program_code',
            'program_discription',
        )
