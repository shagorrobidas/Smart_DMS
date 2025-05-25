from rest_framework import serializers

from Document.models import Template


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = (
            'id',
            'title',
            'code',
        )