from django.urls import path
from apps.reportes.views import actividades_reporte

app_name = 'reportes'

urlpatterns = [
    path('sesion/<int:id_nna>/<int:id_sesion>/', actividades_reporte, name="sesion")
]