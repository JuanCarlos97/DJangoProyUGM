from django.db import models

from django.utils import timezone

# Create your models here.

# Casilla model
class Casilla(models.Model):
    ubicacion = models.CharField(max_length=100)

    class Meta:
        db_table = 'casilla' #Nombre 'casillas' a la tabla en la DB

# Candidato model
class Candidato(models.Model):
    nombrecompleto = models.CharField(max_length=100)
    foto = models.FileField()
    sexo = models.CharField(max_length=1)
    perfil = models.FileField()

    class Meta:
        db_table = 'candidato' #Nombre 'candidatos' a la tabla en la DB