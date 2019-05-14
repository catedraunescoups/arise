from rest_framework.decorators import api_view
from apps.servicios.serializers import UsuarioSerializer, NNASerializer,\
    SesionSerializer, ActividadASerializer, ActividadBSerializer,\
    ActividadCSerializer, ActividadDSerializer, ActividadESerializer,\
    ActividadFSerializer, ActividadGSerializer, ActividadHSerializer
from rest_framework import status, parsers, renderers
from rest_framework.response import Response
from apps.datos.models import NNA
from apps.actividades.models import SESION, ACTIVIDAD_A, ACTIVIDAD_B,\
    ACTIVIDAD_C, ACTIVIDAD_D, ACTIVIDAD_E, ACTIVIDAD_F, ACTIVIDAD_G, ACTIVIDAD_H
from django.contrib.auth.models import User
from django.http.response import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token

# Create your views here.
####### Servicios Web #######

### RECUPERAR PASSWORD ###
### VALIDA USUARIO POR CORREO
@api_view(['POST'])
def validar_Usuario(request):
    response = ""
    try:
        correo = request.data["correo"]
        user = User.objects.get(email=correo)
        if (user != None):
            response = "yes"
        else:
            response = "no"
    except User.DoesNotExist:
        response = "no"
    
    return Response({'response': response})

### CAMBIA LA CLAVE
@api_view(['POST'])
def cambiar_Clave(request):
    response = ""
    try:
        correo = request.data["correo"]
        password = request.data["password"]
        user = User.objects.get(email__exact=correo)
        user.set_password(password)
        user.save()
        response = "yes"
    except User.DoesNotExist:
        response = "no"
    
    return Response({'response': response})

### OBTENER TOKEN ###
class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        token = Token()
        token.key, token.created  = None, None
                
        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key, 'id' : user.id, 'name' : user.first_name + " " + user.last_name })

### REGISTRO DE USUARIO ###
@api_view(['POST'])
def registro_Usuario(request):
    if request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            Token.objects.create(user=usuario)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
### UPDATE Y DELETE USUARIO
@api_view(['GET', 'POST', 'DELETE'])
def update_Usuario(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UsuarioSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    
### REGISTRO DE NNA ###
@api_view(['POST'])
def registro_NNA(request):
    if request.method == 'POST':
        serializer = NNASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### UPDATE NNA
@api_view(['GET', 'POST'])
def update_NNA(request, id):
    try:
        nna = NNA.objects.get(id=id)
    except NNA.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NNASerializer(nna)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NNASerializer(nna, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
 
### DELETE NNA
@api_view(['POST'])
def delete_NNA(request, id):
    try:
        nna = NNA.objects.get(id=id)
    except NNA.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'POST':
        response = ""
        if nna.delete():
            response = "yes"
        else:
            response = "no"
        
        return Response({'deleted': response})

@api_view(['GET'])
def listado_NNA(request, id):
    #muestra los NNA de un solo profesor
    if request.method == 'GET':
        nna = NNA.objects.filter(usuario=id)
        serializer = NNASerializer(nna, many=True)
        return Response(serializer.data)
   
@api_view(['GET', 'POST'])
def registro_sesion(request):
    
    if request.method == 'GET':
        sesion = SESION.objects.filter(persona=id)
        serializer = SesionSerializer(sesion, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SesionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### UPDATE SESION
@api_view(['POST'])
def update_sesion(request, id):
    try:
        sesion = SESION.objects.get(id=id)
    except SESION.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SesionSerializer(sesion, data=data)
        if serializer.is_valid():
            serializer.update(sesion, serializer.validated_data)
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def listado_Sesion(request, id):
    #Lista las sesiones de un NNA
    if request.method == 'GET':
        sesion = SESION.objects.filter(persona=id)
        serializer = SesionSerializer(sesion, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def actividad_A(request):
    if request.method == 'POST':
        serializer = ActividadASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def actividad_B(request):
    if request.method == 'POST':
        serializer = ActividadBSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def actividad_C(request):
    if request.method == 'POST':
        serializer = ActividadCSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def actividad_D(request):
    if request.method == 'POST':
        serializer = ActividadDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def actividad_E(request):
    if request.method == 'POST':
        serializer = ActividadESerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def actividad_F(request):
    if request.method == 'POST':
        serializer = ActividadFSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def actividad_G(request):
    if request.method == 'POST':
        serializer = ActividadGSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def actividad_H(request):
    if request.method == 'POST':
        serializer = ActividadHSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)