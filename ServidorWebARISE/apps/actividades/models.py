from django.db import models
from apps.datos.models import SESION

# Create your models here.
class ACTIVIDAD_A(models.Model):
    sesion=models.ForeignKey(SESION, on_delete=models.CASCADE)
    muycerca=models.IntegerField()
    cerca=models.IntegerField()
    lejos=models.IntegerField()
     
class ACTIVIDAD_B(models.Model):
    sesion=models.ForeignKey(SESION, on_delete=models.CASCADE)
    mano_izquierda=models.IntegerField()
    mano_derecha=models.IntegerField()
    manos_arriba=models.IntegerField()
    manos_abajo=models.IntegerField()
    izquierda=models.IntegerField()
    derecha=models.IntegerField()
    adelante=models.IntegerField()
    atras=models.IntegerField()
    
class ACTIVIDAD_C(models.Model):
    sesion=models.ForeignKey(SESION, on_delete=models.CASCADE)
    cabeza=models.IntegerField()
    boca=models.IntegerField()
    hombros=models.IntegerField()
    pechos=models.IntegerField()
    manos=models.IntegerField()
    vagina=models.IntegerField()
    gluteos=models.IntegerField()
    
class ACTIVIDAD_D(models.Model):
    sesion = models.ForeignKey(SESION, on_delete=models.CASCADE)
    amarillo=models.IntegerField()
    azul=models.IntegerField()
    fucsia=models.IntegerField()
    rojo=models.IntegerField()
    turquesa=models.IntegerField()
    verde=models.IntegerField()

class ACTIVIDAD_E(models.Model):
    sesion = models.ForeignKey(SESION, on_delete=models.CASCADE)
    alegria = models.IntegerField()
    tristeza = models.IntegerField()
    miedo = models.IntegerField()
    sorpresa = models.IntegerField()
    enfado = models.IntegerField()
    
class ACTIVIDAD_F(models.Model):
    sesion = models.ForeignKey(SESION, on_delete=models.CASCADE)
    silencio = models.IntegerField()
    lugar = models.IntegerField()
    saludo = models.IntegerField()
    gracias = models.IntegerField()
    porfavor = models.IntegerField()
    perdon = models.IntegerField()
    disculpe = models.IntegerField()

class ACTIVIDAD_G(models.Model):
    sesion = models.ForeignKey(SESION, on_delete=models.CASCADE)
    aplausos = models.IntegerField()
    zapateos = models.IntegerField()
    golpes = models.IntegerField()

class ACTIVIDAD_H(models.Model):
    sesion = models.ForeignKey(SESION, on_delete=models.CASCADE)
    cero = models.IntegerField()
    uno = models.IntegerField()
    dos = models.IntegerField()
    tres = models.IntegerField()
    cuatro = models.IntegerField()
    cinco = models.IntegerField()
    seis = models.IntegerField()
    siete = models.IntegerField()
    ocho = models.IntegerField()
    nueve = models.IntegerField()
    diez = models.IntegerField()
    once = models.IntegerField()
    doce = models.IntegerField()
    trece = models.IntegerField()
    catorce = models.IntegerField()
    quince = models.IntegerField()
    dieciseis = models.IntegerField()
    diecisiete = models.IntegerField()
    dieciocho = models.IntegerField()
    diecinueve = models.IntegerField()
    veinte = models.IntegerField()