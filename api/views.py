from rest_framework.viewsets import ModelViewSet
from .models import Planta
from .serializer import PlantaSerializer

class PlantaViewSet(ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer
