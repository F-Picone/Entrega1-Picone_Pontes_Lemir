from django.db import models

class medico(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=20)
    sede = models.CharField(max_length=20)

class sede(models.Model):
    especialidad_1 = models.CharField(max_length=20)
    especialidad_2 = models.CharField(max_length=20)
    nombre_sede = models.CharField(max_length=20)

class paciente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()
    obra_social= models.IntegerField()
    sede = models.CharField(max_length=20)