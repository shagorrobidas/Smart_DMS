from rest_framework.generics import ListCreateAPIView
from Document.models import Department
from Document.api.serializers import DepartmentSerializer


class DepatmentListCreateAPIView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
