from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.trailing_slash = '/?'

router.register(r'timers', views.TimerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
