from django.db import models

# Create your models here.

class Posts(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()

    def __str__(self) -> str:
        return self.titulo
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre
    
