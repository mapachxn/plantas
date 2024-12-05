from rest_framework import serializers
from .models import Remedio

class RemedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remedio
        fields = ['id', 'nombre', 'ingredientes', 'receta', 'imagen']
