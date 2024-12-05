from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RemedioViewSet

router = DefaultRouter()
router.register(r'remedios', RemedioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]