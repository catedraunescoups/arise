'''
Created on 8 jun. 2018

@author: usuario
'''
from rest_framework import serializers
from apps.datos.models import NNA
from django.contrib.auth.models import User
from apps.actividades.models import SESION, ACTIVIDAD_A, ACTIVIDAD_B,\
    ACTIVIDAD_D, ACTIVIDAD_E, ACTIVIDAD_F, ACTIVIDAD_G, ACTIVIDAD_H, ACTIVIDAD_C
from datetime import datetime
from arise.settings import DATE_INPUT_FORMATS
from django.template.context_processors import request

class UsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
     
    def create(self, validated_data):
        user = super(UsuarioSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validate_data):
        instance.first_name = validate_data['first_name']
        instance.last_name = validate_data['last_name']
        instance.email = validate_data['email']
        instance.save()
        return instance

class NNASerializer(serializers.ModelSerializer):
    fec_nacimiento = serializers.DateField(input_formats=DATE_INPUT_FORMATS)
    
    class Meta:
        model = NNA
        fields = ('id', 'nombre', 'apellido', 'fec_nacimiento', 'grado', 'usuario')
        
        """def create(self, validated_data):
            datos_obj = NNA(**validated_data)
            datos_obj.save()
            return datos_obj
        
        
        def update(self, instance, validated_data):
            instance.nombre = validated_data['nombre']
            instance.apellido = validated_data['apellido']
            instance.fec_nacimiento = validated_data['fec_nacimiento']
            instance.grado = validated_data['grado']
            instance.usuario = validated_data['usuario']
            instance.save()
            return instance"""

class SesionSerializer(serializers.ModelSerializer):
    fecha_ini = serializers.CharField(required=False)
    fecha_fin = serializers.CharField(required=False)
    
    def create(self, validated_data):
        sesion = SESION(**validated_data)
        sesion.fecha_ini = datetime.now().strftime("%d-%m-%Y %H:%M")
        sesion.fecha_fin = datetime.now().strftime("%d-%m-%Y %H:%M")
        sesion.save()
        return sesion

    def update(self, instance, validated_data):
        instance.fecha_fin = datetime.now().strftime("%d-%m-%Y %H:%M")
        instance.save()
        return instance
    
    class Meta:
        model = SESION
        fields = ('id', 'fecha_ini', 'fecha_fin', 'persona')

class ActividadASerializer(serializers.ModelSerializer):
    class Meta:
        model = ACTIVIDAD_A
        fields = ('muycerca', 'cerca', 'lejos', 'sesion')
        
class ActividadBSerializer(serializers.ModelSerializer):
    class Meta:
        model = ACTIVIDAD_B
        fields = ('mano_izquierda', 'mano_derecha', 'manos_arriba', 'manos_abajo',
                  'izquierda', 'derecha', 'adelante', 'atras', 'sesion')
        
class ActividadCSerializer(serializers.ModelSerializer):
    class Meta:
        model = ACTIVIDAD_C
        fields = ('cabeza', 'boca', 'hombros', 'pechos', 'manos', 'vagina', 'gluteos', 'sesion')
           
class ActividadDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ACTIVIDAD_D
        fields = ('amarillo', 'azul', 'fucsia', 'rojo', 'turquesa', 'verde', 'sesion')
        
class ActividadESerializer(serializers.ModelSerializer):
    class Meta:
        model = ACTIVIDAD_E
        fields = ('alegria', 'tristeza', 'miedo', 'sorpresa', 'enfado', 'sesion')
        
class ActividadFSerializer(serializers.ModelSerializer):
    class Meta:
        model = ACTIVIDAD_F
        fields = ('silencio', 'lugar', 'saludo', 'gracias', 'porfavor', 'perdon', 'disculpe', 'sesion')
        
class ActividadGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ACTIVIDAD_G
        fields = ('aplausos', 'zapateos', 'golpes', 'sesion') 
        
class ActividadHSerializer(serializers.ModelSerializer):
    class Meta:
        model = ACTIVIDAD_H
        fields = ('cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve',
                   'diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciseis', 'diecisiete',
                  'dieciocho', 'diecinueve', 'veinte', 'sesion')     