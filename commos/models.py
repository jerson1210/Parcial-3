from django.db import models

class Notas(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nota = models.PositiveSmallIntegerField()
    fecha = models.DateField()

class Usuario(models.Model):
    
