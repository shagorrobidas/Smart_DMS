from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from Document.models import University
from Document.api.serializers import UniversitySerializer


class UniversityListCreateAPIView(ListCreateAPIView):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()
