from rest_framework.generics import ListCreateAPIView
from Document.models import Template
from Document.api.serializers import TemplateSerializer


class TemplateListCreateAPIView(ListCreateAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    