from rest_framework import viewsets
from django.views.generic import View
from django.shortcuts import render
from depts.models import Depts


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .serializers import DeptsSerializer
# Create your views here.

class Index(View):
    @method_decorator(login_required)
    def get(self,request):
        #個々の記述を考える
        return render(request,'login.html')
class DeptsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Depts.objects.all()
    serializer_class = DeptsSerializer
