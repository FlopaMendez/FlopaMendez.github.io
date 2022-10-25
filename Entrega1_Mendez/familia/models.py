from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    dni = models.IntegerChoices(null=True)

class Clientes(models.Model):
    nombre_empresas = models.CharField(max_length=100)
    cuit = models.IntegerField()
    email = models.EmailField()
    fecha_alta_cliente = models.DateField()
    facturacion_mensual = models.IntegerField()