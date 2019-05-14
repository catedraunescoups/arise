from django.shortcuts import render, redirect
from apps.utilidades.utils import crear_html, generarTituloPrincipal,\
    guardar_html, formated_age, generarTabla, finalizar_html, existe_html,\
    render_to_pdf
from django.http.response import HttpResponse
from datetime import datetime
from django.utils import timezone

# Create your views here.
def reporte_sesion_html(id_sesion, fecha_ini, fecha_fin, cabecera, actA, actB, actC, actD, actE, actF, actG, actH):
    nombre = 'sesion' +str(id_sesion)+ '.html' 
    fichero = crear_html(nombre)
    titulo_principal = generarTituloPrincipal('ESCUELA "SOR TERESA VALSÉ"')
    guardar_html(fichero, titulo_principal)
    
    if fichero != None:
        if cabecera.fec_nacimiento != None:
            nacimiento = formated_age(cabecera.fec_nacimiento)
        else:
            nacimiento = ''
            
        estructura = []
        estructura.append([':b:Nombres y Apellidos: ',cabecera.nombre+' '+cabecera.apellido])
        estructura.append([':b:Fecha de Nacimiento: ',nacimiento])
        estructura.append([':b:Grado: ',cabecera.grado])
        estructura.append([':b:Fecha de Inicio de la Sesión: ', fecha_ini])
        estructura.append([':b:Fecha de Término de la Sesión: ', fecha_fin])
        tablaCabecera = generarTabla(estructura, 'DATOS PERSONALES', borde=0)
        guardar_html(fichero, tablaCabecera)
        
        ### ACTIVIDAD A ###
        if actA != None:
            estructura = []
            estructura.append([':b:Muy Cerca', actA['muycerca']])
            estructura.append([':b:Cerca', actA['cerca']])
            estructura.append([':b:Lejos', actA['lejos']])
            
            tablaA = generarTabla(estructura, 'ÁREA 1: ESPACIO PERSONAL')
            guardar_html(fichero, tablaA)
        
        ### ACTIVIDAD B ###
        if actB != None:
            estructura = []
            estructura.append([':b:Mano Izquierda', actB['mano_izquierda']])
            estructura.append([':b:Mano Derecha', actB['mano_derecha']])
            estructura.append([':b:Manos Arriba', actB['manos_arriba']])
            estructura.append([':b:Manos Abajo', actB['manos_abajo']])
            estructura.append([':b:Izquierda', actB['izquierda']])
            estructura.append([':b:Derecha', actB['derecha']])
            estructura.append([':b:Adelante', actB['adelante']])
            estructura.append([':b:Atrás', actB['atras']])
            
            tablaB = generarTabla(estructura, 'ÁREA 2: LATERALIDAD')
            guardar_html(fichero, tablaB)
        
        ### ACTIVIDAD C ###
        if actC != None:
            estructura = []
            estructura.append([':b:Cabeza', actC['cabeza']])
            estructura.append([':b:Boca', actC['boca']])
            estructura.append([':b:Hombros', actC['hombros']])
            estructura.append([':b:Pechos', actC['pechos']])
            estructura.append([':b:Manos', actC['manos']])
            estructura.append([':b:Vagina', actC['vagina']])
            estructura.append([':b:Glúteos', actC['gluteos']])
            
            tablaC = generarTabla(estructura, 'ÁREA 3: PARTES DEL CUERPO')
            guardar_html(fichero, tablaC)
        
        ### ACTIVIDAD D ###
        if actD != None:
            estructura = []
            estructura.append([':b:Amarillo', actD['amarillo']])
            estructura.append([':b:Azul', actD['azul']])
            estructura.append([':b:Fucsia', actD['fucsia']])
            estructura.append([':b:Rojo', actD['rojo']])
            estructura.append([':b:Turquesa', actD['turquesa']])
            estructura.append([':b:Verde', actD['verde']])
            
            tablaD = generarTabla(estructura, 'ÁREA 4: COLORES')
            guardar_html(fichero, tablaD)
        
        ### ACTIVIDAD E ###
        if actE != None:
            estructura = []
            estructura.append([':b:Alegría', actE['alegria']])
            estructura.append([':b:Tristeza', actE['tristeza']])
            estructura.append([':b:Miedo', actE['miedo']])
            estructura.append([':b:Sorpresa', actE['sorpresa']])
            estructura.append([':b:Enfado', actE['enfado']])
            
            tablaE = generarTabla(estructura, 'ÁREA 5: EMOCIONES')
            guardar_html(fichero, tablaE)
        
        ### ACTIVIDAD F ###
        if actF != None:
            estructura = []
            estructura.append([':b:Silencio', actF['silencio']])
            estructura.append([':b:En su lugar', actF['lugar']])
            estructura.append([':b:Saludo', actF['saludo']])
            estructura.append([':b:Gracias', actF['gracias']])
            estructura.append([':b:Por Favor', actF['porfavor']])
            estructura.append([':b:Perdón', actF['perdon']])
            estructura.append([':b:Disculpe', actF['disculpe']])
            
            tablaF = generarTabla(estructura, 'ÁREA 6: NORMAS DE BUENA EDUCACIÓN')
            guardar_html(fichero, tablaF)
        
        ### ACTIVIDAD G ###
        if actG != None:
            estructura = []
            estructura.append([':b:Aplausos', actG['aplausos']])
            estructura.append([':b:Zapateos', actG['zapateos']])
            estructura.append([':b:Golpes', actG['golpes']])
            
            tablaG= generarTabla(estructura, 'ÁREA 7: SECUENCIAS RÍTMICAS')
            guardar_html(fichero, tablaG)
        
        ### ACTIVIDAD H ###
        if actH != None:
            estructura = []
            estructura.append([':b:Número Cero', actH['cero']])
            estructura.append([':b:Número Uno', actH['uno']])
            estructura.append([':b:Número Dos', actH['dos']])
            estructura.append([':b:Número Tres', actH['tres']])
            estructura.append([':b:Número Cuatro', actH['cuatro']])
            estructura.append([':b:Número Cinco', actH['cinco']])
            estructura.append([':b:Número Seis', actH['seis']])
            estructura.append([':b:Número Siete', actH['siete']])
            estructura.append([':b:Número Ocho', actH['ocho']])
            estructura.append([':b:Número Nueve', actH['nueve']])
            estructura.append([':b:Número Diez', actH['diez']])
            estructura.append([':b:Número Once',  actH['once']])
            estructura.append([':b:Número Doce', actH['doce']])
            estructura.append([':b:Número Trece', actH['trece']])
            estructura.append([':b:Número Catorce', actH['catorce']])
            estructura.append([':b:Número Quince', actH['quince']])
            estructura.append([':b:Número Diez y Seis', actH['dieciseis']])
            estructura.append([':b:Número Diez y Siete', actH['diecisiete']])
            estructura.append([':b:Número Diez y Ocho', actH['dieciocho']])
            estructura.append([':b:Número Diez y Nueve', actH['diecinueve']])
            estructura.append([':b:Número Veinte', actH['veinte']])
            
            tablaH = generarTabla(estructura, 'ÁREA 8: NÚMEROS')
            guardar_html(fichero, tablaH)
            
            finalizar_html(fichero)

#################################################################
def reporte_sesion_pdf(request, id_sesion):
    nombre = 'sesion' + str(id_sesion)+ '.html'  
    data = {'titulo' : 'Reporte Sesiones'}
    
    if existe_html(nombre):
        print(nombre)
        print(id_sesion)
        pdf = render_to_pdf('vertical', 'aux/'+nombre, data)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'filename=sesion'+str(id_sesion)+'.pdf'
            return response
    else:
        return redirect('error', id_sesion=id_sesion)
