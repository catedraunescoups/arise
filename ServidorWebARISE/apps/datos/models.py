from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NNA(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=70, blank=False, null=False)
    apellido = models.CharField(max_length=70, blank=False, null=False)
    fec_nacimiento = models.DateField(blank=False, null=False)
    grado = models.CharField(max_length=10, blank=False, null=False)

class SESION(models.Model):
    persona = models.ForeignKey(NNA, on_delete=models.CASCADE)
    fecha_ini = models.CharField(max_length=16, blank=False, null=False)
    fecha_fin = models.CharField(max_length=16, blank=False, null=False)