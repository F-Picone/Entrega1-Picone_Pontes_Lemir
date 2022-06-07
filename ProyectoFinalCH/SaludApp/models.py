from unittest.mock import MagicMixin
from django.db import models

class medico(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=20)
    sede = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombre+" "+str(self.especialidad)

class sede(models.Model):
    lugar= models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.lugar

class paciente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()
    obra_social= models.CharField(max_length=20)
    sede = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.nombre+" "+str(self.dni)