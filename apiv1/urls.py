from django.urls import path,include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('depts',views.DeptsViewSet)

app_name = 'apiv1'
urlpatterns =[
    path('',include(router.urls))
]