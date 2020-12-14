from rest_framework import viewsets

from depts.models import Depts
from .serializers import DeptsSerializer
# Create your views here.

class DeptsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Depts.objects.all()
    serializer_class = DeptsSerializer
