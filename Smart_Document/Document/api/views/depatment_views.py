from rest_framework.generics import ListAPIView
from Document.models import Department
from Document.api.serializers import DepartmentSerializer


class DepatmentListView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
