from rest_framework.generics import ListCreateAPIView
from Document.models import University
from Document.api.serializers import UniversitySerializer


class UniversityListCreateAPIView(ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer