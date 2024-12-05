from django.db import models

class Remedio(models.Model):
    nombre = models.CharField(max_length=100)
    ingredientes = models.TextField()
    receta = models.CharField(max_length=100)  # Cambia según la relación que necesites
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)  # Campo para la imagen
    
    def __str__(self):
        return self.nombre
