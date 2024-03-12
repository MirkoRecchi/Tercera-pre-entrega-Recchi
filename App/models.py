from django.db import models

# Create your models here.

class Participante(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    edad= models.IntegerField()

class Jurado(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)

class Libro(models.Model):
    nombre= models.CharField(max_length=20)
    cantidadLetras= models.IntegerField()

class Calificacion(models.Model):
    nota = models.IntegerField()
    nombreJurado= models.CharField(max_length=20)
    nombreLibro = models.CharField(max_length=20, default='DEFAULT VALUE')
    



    







