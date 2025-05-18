from rest_framework.generics import ListCreateAPIView
from Document.models import Position
from Document.api.serializers import PositionSerializer


class PositionListCreateAPIView(ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


