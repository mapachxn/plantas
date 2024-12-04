from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlantaViewSet

router = DefaultRouter()
router.register(r'planta', PlantaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
