from django.urls.conf import path
from apps.servicios.views import registro_Usuario, registro_NNA, listado_NNA,\
    update_Usuario, update_NNA, ObtainAuthToken, delete_NNA, validar_Usuario,\
    cambiar_Clave, registro_sesion, listado_Sesion, actividad_A, actividad_B,\
    actividad_C, actividad_D, actividad_E, actividad_F, actividad_G, actividad_H,\
    update_sesion
app_name = 'servicios'

urlpatterns = [
    # Login
    path('api-token-auth/', ObtainAuthToken.as_view(), name='token'),
    # Validacion Usuario
    path('validarUsuario/', validar_Usuario, name='validar'),
    # Cambio clave
    path('cambiarClave/', cambiar_Clave, name='cambiar_clave'),
    # Profesor
    path('addProfesor/', registro_Usuario, name="addProfesor"),
    path('updateProfesor/<int:id>/', update_Usuario, name="updateProfesor"),
    # ALumno
    path('addAlumno/', registro_NNA, name="addAlumno"),
    path('listAlumnos/<int:id>/', listado_NNA, name="listAlumnos"),
    path('updateAlumno/<int:id>/', update_NNA, name="updateAlumno"),
    path('deleteAlumno/<int:id>/', delete_NNA, name="deleteAlumno"),
    # Sesion
    path('addSesion/', registro_sesion, name="addSesion"),
    path('updateSesion/<int:id>/', update_sesion, name="updateSesion"),
    path('listSesiones/<int:id>/', listado_Sesion, name="listSesiones"),
    ## Actividades de la Sesion
    path('addActividadA/', actividad_A, name="addActividadA"),
    path('addActividadB/', actividad_B, name="addActividadB"),
    path('addActividadC/', actividad_C, name="addActividadC"),
    path('addActividadD/', actividad_D, name="addActividadD"),
    path('addActividadE/', actividad_E, name="addActividadE"),
    path('addActividadF/', actividad_F, name="addActividadF"),
    path('addActividadG/', actividad_G, name="addActividadG"),
    path('addActividadH/', actividad_H, name="addActividadH"),
]