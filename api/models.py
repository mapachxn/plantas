from django.db import models

class Planta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)  # Campo para la imagen

    def __str__(self):
        return self.nombre
