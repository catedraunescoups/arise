from django.shortcuts import render
from apps.datos.models import SESION, NNA
from apps.utilidades.views import reporte_sesion_html, reporte_sesion_pdf
from apps.actividades.models import ACTIVIDAD_A, ACTIVIDAD_C, ACTIVIDAD_B,\
    ACTIVIDAD_D, ACTIVIDAD_E, ACTIVIDAD_F, ACTIVIDAD_G, ACTIVIDAD_H
from django.db.models.aggregates import Sum
from django.http.response import HttpResponse
from datetime import datetime

# Create your views here.
def isDataEmpty(data):
    check = False
    for key, value in data.items():
        if value == None:
            check = True
            break
    
    return check

def actividades_reporte(request, id_nna, id_sesion):
    try:
        dato = NNA.objects.get(id=id_nna)
        
        if dato != None:
            sesion = SESION.objects.get(id=id_sesion)
            if sesion != None:
                actA = {}
                actB = {}
                actC = {}
                actD = {}
                actE = {}
                actF = {}
                actG = {}
                actH = {}
                actA['muycerca'] = ACTIVIDAD_A.objects.filter(sesion=id_sesion).aggregate(Sum('muycerca'))['muycerca__sum']
                actA['cerca'] = ACTIVIDAD_A.objects.filter(sesion=id_sesion).aggregate(Sum('cerca'))['cerca__sum']
                actA['lejos'] = ACTIVIDAD_A.objects.filter(sesion=id_sesion).aggregate(Sum('lejos'))['lejos__sum']
                
                actB['mano_izquierda'] = ACTIVIDAD_B.objects.filter(sesion=id_sesion).aggregate(Sum('mano_izquierda'))['mano_izquierda__sum']
                actB['mano_derecha'] = ACTIVIDAD_B.objects.filter(sesion=id_sesion).aggregate(Sum('mano_derecha'))['mano_derecha__sum']
                actB['manos_arriba'] = ACTIVIDAD_B.objects.filter(sesion=id_sesion).aggregate(Sum('manos_arriba'))['manos_arriba__sum']
                actB['manos_abajo'] = ACTIVIDAD_B.objects.filter(sesion=id_sesion).aggregate(Sum('manos_abajo'))['manos_abajo__sum']
                actB['izquierda'] = ACTIVIDAD_B.objects.filter(sesion=id_sesion).aggregate(Sum('izquierda'))['izquierda__sum']
                actB['derecha'] = ACTIVIDAD_B.objects.filter(sesion=id_sesion).aggregate(Sum('derecha'))['derecha__sum']
                actB['adelante'] = ACTIVIDAD_B.objects.filter(sesion=id_sesion).aggregate(Sum('adelante'))['adelante__sum']
                actB['atras'] = ACTIVIDAD_B.objects.filter(sesion=id_sesion).aggregate(Sum('atras'))['atras__sum']
                
                actC['cabeza'] = ACTIVIDAD_C.objects.filter(sesion=id_sesion).aggregate(Sum('cabeza'))['cabeza__sum']
                actC['boca'] = ACTIVIDAD_C.objects.filter(sesion=id_sesion).aggregate(Sum('boca'))['boca__sum']
                actC['hombros'] = ACTIVIDAD_C.objects.filter(sesion=id_sesion).aggregate(Sum('hombros'))['hombros__sum']
                actC['pechos'] = ACTIVIDAD_C.objects.filter(sesion=id_sesion).aggregate(Sum('pechos'))['pechos__sum']
                actC['manos'] = ACTIVIDAD_C.objects.filter(sesion=id_sesion).aggregate(Sum('manos'))['manos__sum']
                actC['vagina'] = ACTIVIDAD_C.objects.filter(sesion=id_sesion).aggregate(Sum('vagina'))['vagina__sum']
                actC['gluteos'] = ACTIVIDAD_C.objects.filter(sesion=id_sesion).aggregate(Sum('gluteos'))['gluteos__sum']
                
                actD['amarillo'] = ACTIVIDAD_D.objects.filter(sesion=id_sesion).aggregate(Sum('amarillo'))['amarillo__sum']
                actD['azul'] = ACTIVIDAD_D.objects.filter(sesion=id_sesion).aggregate(Sum('azul'))['azul__sum']
                actD['fucsia'] = ACTIVIDAD_D.objects.filter(sesion=id_sesion).aggregate(Sum('fucsia'))['fucsia__sum']
                actD['rojo'] = ACTIVIDAD_D.objects.filter(sesion=id_sesion).aggregate(Sum('rojo'))['rojo__sum']
                actD['turquesa'] = ACTIVIDAD_D.objects.filter(sesion=id_sesion).aggregate(Sum('turquesa'))['turquesa__sum']
                actD['verde'] = ACTIVIDAD_D.objects.filter(sesion=id_sesion).aggregate(Sum('verde'))['verde__sum']
                
                actE['alegria'] = ACTIVIDAD_E.objects.filter(sesion=id_sesion).aggregate(Sum('alegria'))['alegria__sum']
                actE['tristeza'] = ACTIVIDAD_E.objects.filter(sesion=id_sesion).aggregate(Sum('tristeza'))['tristeza__sum']
                actE['miedo'] = ACTIVIDAD_E.objects.filter(sesion=id_sesion).aggregate(Sum('miedo'))['miedo__sum']
                actE['sorpresa'] = ACTIVIDAD_E.objects.filter(sesion=id_sesion).aggregate(Sum('sorpresa'))['sorpresa__sum']
                actE['enfado'] = ACTIVIDAD_E.objects.filter(sesion=id_sesion).aggregate(Sum('enfado'))['enfado__sum']
                
                actF['silencio'] = ACTIVIDAD_F.objects.filter(sesion=id_sesion).aggregate(Sum('silencio'))['silencio__sum']
                actF['lugar'] = ACTIVIDAD_F.objects.filter(sesion=id_sesion).aggregate(Sum('lugar'))['lugar__sum']
                actF['saludo'] = ACTIVIDAD_F.objects.filter(sesion=id_sesion).aggregate(Sum('saludo'))['saludo__sum']
                actF['gracias'] = ACTIVIDAD_F.objects.filter(sesion=id_sesion).aggregate(Sum('gracias'))['gracias__sum']
                actF['porfavor'] = ACTIVIDAD_F.objects.filter(sesion=id_sesion).aggregate(Sum('porfavor'))['porfavor__sum']
                actF['perdon'] = ACTIVIDAD_F.objects.filter(sesion=id_sesion).aggregate(Sum('perdon'))['perdon__sum']
                actF['disculpe'] = ACTIVIDAD_F.objects.filter(sesion=id_sesion).aggregate(Sum('disculpe'))['disculpe__sum']
                
                actG['aplausos'] = ACTIVIDAD_G.objects.filter(sesion=id_sesion).aggregate(Sum('aplausos'))['aplausos__sum']
                actG['zapateos'] = ACTIVIDAD_G.objects.filter(sesion=id_sesion).aggregate(Sum('zapateos'))['zapateos__sum']
                actG['golpes'] = ACTIVIDAD_G.objects.filter(sesion=id_sesion).aggregate(Sum('golpes'))['golpes__sum']
                
                actH['cero'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('cero'))['cero__sum']
                actH['uno'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('uno'))['uno__sum']
                actH['dos'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('dos'))['dos__sum']
                actH['tres'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('tres'))['tres__sum']
                actH['cuatro'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('cuatro'))['cuatro__sum']
                actH['cinco'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('cinco'))['cinco__sum']
                actH['seis'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('seis'))['seis__sum']
                actH['siete'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('siete'))['siete__sum']
                actH['ocho'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('ocho'))['ocho__sum']
                actH['nueve'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('nueve'))['nueve__sum']
                actH['diez'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('diez'))['diez__sum']
                actH['once'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('once'))['once__sum']
                actH['doce'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('doce'))['doce__sum']
                actH['trece'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('trece'))['trece__sum']
                actH['catorce'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('catorce'))['catorce__sum']
                actH['quince'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('quince'))['quince__sum']
                actH['dieciseis'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('dieciseis'))['dieciseis__sum']
                actH['diecisiete'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('diecisiete'))['diecisiete__sum']
                actH['dieciocho'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('dieciocho'))['dieciocho__sum']
                actH['diecinueve'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('diecinueve'))['diecinueve__sum']
                actH['veinte'] = ACTIVIDAD_H.objects.filter(sesion=id_sesion).aggregate(Sum('veinte'))['veinte__sum']
                
                ### Comprobar Contenido de Diccionarios ###
                if isDataEmpty(actA) == True:
                    actA = None
                
                if isDataEmpty(actB) == True:
                    actB = None
                 
                if isDataEmpty(actC) == True:
                    actC = None
                
                if isDataEmpty(actD) == True:
                    actD = None   
                
                if isDataEmpty(actE) == True:
                    actE = None
                
                if isDataEmpty(actF) == True:
                    actF = None
                
                if isDataEmpty(actG) == True:
                    actG = None
                
                if isDataEmpty(actH) == True:
                    actH = None
                ### Crear fichero html ###
                reporte_sesion_html(id_sesion, sesion.fecha_ini, sesion.fecha_fin, dato, actA, actB, actC, actD, actE, actF, actG, actH)
                return reporte_sesion_pdf(request, id_sesion)
    except NNA.DoesNotExist:
        return HttpResponse(status=404)

        