from rest_framework.generics import ListCreateAPIView
from Document.models import Program
from Document.api.serializers import ProgramSerializer


class ProgramListCreateAPIView(ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
