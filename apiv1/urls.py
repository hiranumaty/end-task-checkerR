from django.urls import path,include
from rest_framework import routers
from django.contrib.auth.views import LoginView,logout_then_login
from . import views

router = routers.DefaultRouter()
router.register('depts',views.DeptsViewSet)

app_name = 'apiv1'
urlpatterns =[
    path('login/',LoginView.as_view(template_name="login.html"),name='login'),
    #path('',include(router.urls))
]