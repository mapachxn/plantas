from rest_framework.viewsets import ModelViewSet
from .models import Remedio
from .serializer import RemedioSerializer

class RemedioViewSet(ModelViewSet):
    queryset = Remedio.objects.all()
    serializer_class = RemedioSerializer
