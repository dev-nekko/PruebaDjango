
from django.urls import path
from DashboardDjangoSoftware.views import saludos, despedida, ObtenerFecha, calcularEdad
from . import views

urlpatterns = [
    path('saludos/', saludos),
    path('nosveremos/', despedida),
    path('fecha/', ObtenerFecha),
    path('edades/<int:edad>/<int:year>', calcularEdad),
    path('', views.ruta),
    path('reconocimiento/', views.reconocimiento ),
]
